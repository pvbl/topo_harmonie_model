def plot_geotiff(file_name,file_2,step=50):
		##Extracts variables from raster
		from osgeo import gdal,osr
		import matplotlib.pyplot as plt
		from numpy import linspace
		
		dataset=gdal.Open(file_name, gdal.GA_ReadOnly)	
		band=dataset.GetRasterBand(1)
		#rows and columns of the file
		height = band.XSize
		width= band.YSize
		#get Coordinates and convert it to WGS84
		gt = dataset.GetGeoTransform()  
		minX=gt[0];
		minY=gt[3] + width*gt[4] + height*gt[5];
		maxX=gt[0] + width*gt[1] + height*gt[2];
		maxY=gt[3];
		elevation=band.ReadAsArray()
		extent=[minX,maxX,minY,maxY]
		plt.imshow(elevation[::step,::step], cmap='gist_earth', extent=extent)
		dataset=gdal.Open(file_2, gdal.GA_ReadOnly)	
		band=dataset.GetRasterBand(1)
		height = band.XSize
		width= band.YSize
		##get Coordinates and convert it to WGS84
		gt = dataset.GetGeoTransform()  
		minX=gt[0];
		minY=gt[3] + width*gt[4] + height*gt[5];
		maxX=gt[0] + width*gt[1] + height*gt[2];
		maxY=gt[3];
		elevation=band.ReadAsArray()
		rasterMin, rasterMax=band.ComputeRasterMinMax()
		print rasterMin
		levels=linspace(rasterMin,1,1)
		extent= [minX,maxX,minY,maxY]
		plt.contour(elevation[::-1], levels, hold='on', colors = 'w', origin='lower', extent=extent)
		plt.title('EU-DEM y GTOPO30 (contorno)')
		plt.xlabel('longitud')
		plt.ylabel('latitud')
		plt.savefig('figure_raster.png')
		plt.close()