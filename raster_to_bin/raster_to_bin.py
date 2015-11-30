
#************************************************
########CONVERT  RASTER TO HARMONIE BINARIES############
#***************************************************
#
#  Project: Introduce High Resolution Topography into HARMONIE model 
#
#  Purpose: Script to convert raster files to binary files
# for HARMONIE model
#
#
#  Author:  Paul Van Branteghem, paulvanlorenzo@hotmail.com
#            Intership AEMET
#
#  DEPENDENCES: gdal, osr, numpy
#
#  INFORMATION:before running this script, merge or crop the geotiff
# to the interested domain using gdal utilities.
#
#  How to run the script: python raster_to_bin.py \path\to\geotiff.tif
#***************************************************



def create_all(file_name):
	##Extracts variables from raster
	from osgeo import gdal,osr
	check_file(file_name)
	dataset=gdal.Open(file_name, gdal.GA_ReadOnly)	
	band=dataset.GetRasterBand(1)
	#columns  and rows of the file
	cols = band.XSize
	rows= band.YSize
	#get Coordinates and convert it to WGS84
	gt = dataset.GetGeoTransform()  
	src_srs=osr.SpatialReference()
	src_srs.ImportFromWkt(dataset.GetProjection())
	BandType = gdal.GetDataTypeName(band.DataType)
	tgt_srs = osr.SpatialReference()
	tgt_srs.SetWellKnownGeogCS("WGS84")
	tgt_srs=tgt_srs.CloneGeogCS()
	#Get the borders of the raster
	ext=GetExtent(gt,rows,cols)
	#change projection to WGS84
	geo_ext=ReprojectCoords(ext,src_srs,tgt_srs)
	####Create all
	#Create the header of the binary
	create_header(rows,cols,geo_ext)	
	##create binary
	create_bin_HARMONIE(cols,rows,band)


def GetExtent(gt,rows,cols):
    ###Get the borders of the raster
    ext=[]
    xarr=[0,cols]
    yarr=[0,rows]
    #Pixels from borders
    for px in xarr:
        for py in yarr:
            x=gt[0]+(px*gt[1])+(py*gt[2])
            y=gt[3]+(px*gt[4])+(py*gt[5])
            ext.append([x,y])
        yarr.reverse()
    return ext

def ReprojectCoords(coords,src_srs,tgt_srs):
    ###Change (if necessary by itself) the projection to WGS84 
    from osgeo import osr
    trans_coords=[]
    transform = osr.CoordinateTransformation( src_srs, tgt_srs)
    for x,y in coords:
        x,y,z = transform.TransformPoint(x,y)
        trans_coords.append([x,y])
    print 'Cordenadas del raster:'
    print 'Norte : {}'.format(trans_coords[0][1])
    print 'Sur : {}'.format(trans_coords[1][1])
    print 'Este : {}'.format(trans_coords[3][0])
    print 'Oeste : {}'.format(trans_coords[0][0])
    return trans_coords




def create_header(rows,cols,geo_ext):
	#Build Harmonie Binary Header
	hd=open('header.hdr','w')
	north=round(geo_ext[0][1],5);
	south=round(geo_ext[1][1],5);
	east=round(geo_ext[3][0] ,5);
	west=round(geo_ext[0][0] ,5);
	hd.write("ASTER topography model, starting UL\n")
	hd.write("nodata: -9999\n")
	hd.write("north: {} \n".format(north))
	hd.write("south: {} \n".format(south))
	hd.write("west:  {} \n".format(west))
	hd.write("east:  {} \n".format(east))
	hd.write("rows:  {} \n".format(rows))
	hd.write("cols:  {} \n".format(cols))
	hd.write("recordtype: integer 16 bits\n")
	hd.close()	
	print 'Se ha generado la cabecera para el Harmonie'


def create_bin_HARMONIE(cols,rows,band):
	#Build the binarie 
	import struct, numpy as np
	fh=open('harmonie.dir','wb')
	print 'Se procede a crear el binario'
	for j in xrange(rows):
		#band.ReasAsArray() is the elevation
		#Extracted in rows for a efficiently memory read
		elevation=band.ReadAsArray(0,j,cols,1)
		for i in xrange(cols):
			fh.write(struct.pack('>h',elevation[0][i]))
	print 'El binario se ha generado'
	fh.close()


def check_file(file_name):
#Check if file exists
	from sys import exit
	from os import path
	if path.isfile(file_name):
		print 'The geotiff is '+file_name
	else:
		print "The file "
		print  file_name 
		print "  doesn't exists"
		exit(0)	


if __name__=='__main__':
	from sys import argv
	create_all(argv[1])
else:
	print "run create_all(file_name) to convert"
	