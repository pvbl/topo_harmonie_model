#************************************************
########BUILD  BINARIES FOR HARMONIE MODEL && PLOT  RASTER AND BINARIES############
#***************************************************
#
#  Project: Introduce High Resolution Topography into HARMONIE model 
#
#  Purpose: Script to plot raster files and HARMONIE binary files
# 
#
#
#  Author:  Paul Van Branteghem, paulvanlorenzo@hotmail.com
#            Intership AEMET
#
#  DEPENDENCES: gdal, matplotlib, numpy, and TOPO_HARMONIE file
#
#  INFORMATION:before running this script, merge or crop the geotiff
# to the interested domain using gdal utilities.
#
#  How to run the script:
#
# put in the same path as the folder TOPO_HARMONIE (it’s also possible
# to put it in your python path)
# If you want to create a binary file from geotiff file:
#  from raster_to_bin.raster_to_bin import create_all
#run:
#create_all(<path/to/tif/file.tif>)
# PLOT TIF FILES:
#file_name='path/to/tif'
#resolution is the resolution in degrees for big data files
#if resolution=None is the same size as the tif
#shaded_relief(file_name) plot in shaded relief image
#slope_relief(file_name) plot in slope relief
#
#It's possible to plot eu-dem shaded 
#
#
#PLOT BINARY
#hed_name='/path/of/header.hdr'
#bin_name='path/of/binary.dir'
#step=50
#
#
# COMMENTS: If you want to create binary files from geotiff files in commands line: 
# the easier way is using the script: TOPO_HARMONIE/raster_to_bin/raster_to_bin.py
# put in commands line:
# python raster_to_bin.py <path/to/tif/file.tif>
#***************************************************



from TOPO_HARMONIE import *
##############CREATE HARMONIE BINARIES#########
###Uncoment this section to convert geotiff to binary
# from raster_to_bin.raster_to_bin import create_all
#file='path/to/tif/file.tif'
#create_all(file)




######PLOT TIF FILES##################


###Uncoment this section to plot tif files

#Path of file
#file_name='path/to/tif/file.tif'

###PARAMETERS
# If you want to resize in put resolution geocoordinates, else resolution=None
resolution=0.1
#resolution=None

#If you want to define a domain coord=[xmin,ymin,xmax,ymax]; else put coord=None
coord=[-8.95, 42, -8.6, 42.35 ]
#coord=None



#file_name=plots.resize_tif(file_name,resolution,coord)
#plots.raster.shaded_relief(file_name)
#plots.raster.slope_relief(file_name)
#from os import remove
#remove('./resized.tif')


####Plot EU-DEM and GTOPO30 contours both.
#file_name='eudem.tif'
#file_2='gtopo30.tif'
#plot_tiff().plot_geotiff(file_name,file_2,step=50)


######PLOT BINARY FILES##################
###Uncoment this section to plot binary files
#hed_name='./gtopo30.hdr'
#bin_name='./gtopo30.dir'
#step=10
#extent=[-20,20,0,90]
#plots.binary.plot_binary_data(bin_name,hed_name,step,extent)
