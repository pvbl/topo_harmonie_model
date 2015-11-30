def shaded_relief(file_name):
		from os import system, path
		system('gdaldem hillshade -co compress=lzw {} shaded_dem.tif'.format(file_name))


def slope_relief(file_name):
		from os import path, system, remove
		from osgeo import gdal
		from numpy import linspace
		dataset=gdal.Open(file_name, gdal.GA_ReadOnly)
		band=dataset.GetRasterBand(1)
		rasterMin, rasterMax=band.ComputeRasterMinMax()
	
		num_col=7
		minmax=linspace(rasterMin,rasterMax,num_col)
		f=open('colors.txt','w')
		f.write('{} 16  78 139 \n'.format(0))
		f.write('{} 47 79 79 \n'.format(int(minmax[0])))
		f.write('{} 254 254 254 \n'.format(int(minmax[1])))
		f.write('{} 121 117 10 \n'.format(int(minmax[2])))
		f.write('{} 151 106 47 \n'.format(int(minmax[3])))
		f.write('{} 127 166 122 \n'.format(int(minmax[4])))
		f.write('{} 213 213 149 \n'.format(int(minmax[5])))
		f.write('{} 218 179 122 \n'.format(int(minmax[6])))
		f.close()
		system('gdaldem color-relief {} colors.txt relief.tif'.format(file_name))
		remove('colors.txt')



def resize_tif(file_name,resolution='None',coord='None'):
		from os import system
		if resolution==None:
			tr=' '
		else:
			tr='-tr {} {} '.format(resolution,resolution)
		
		if coord==None:
			te=' '
		elif coord!=None:
			te='-te {}'.format("".join(' {:.2f} '.format(i) for i in coord))	
		
		if resolution!=None or coord!=None:						
			argm='gdalwarp {} {} {} resized.tif'.format(te,tr,file_name)	
			print argm
			system(argm)	
			file_name='./resized.tif'
		return file_name