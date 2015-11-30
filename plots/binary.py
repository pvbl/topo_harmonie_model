def plot_binary_data(bin_name,hed_name,step,extent):
	import numpy as np
	import matplotlib.pyplot as plt
	with open(hed_name,'r') as openfile:
		print 'File values'
		for line in openfile:
			for srd in line.split():
				if "north:" in srd:
					north=float(line.split()[1])
					print "north: "+str(north)
				elif "south:" in srd:
					south=float(line.split()[1])
					print "south: "+str(south)
				elif "west:" in srd:
					west=float(line.split()[1])
					print "west: "+str(west)
				elif "east:" in srd:
					east=float(line.split()[1])
					print "east: "+str(east)
				elif "rows:" in srd:
					rows=int(line.split()[1])
					print "rows: "+ str(rows)
				elif "cols:" in srd:
					cols=int(line.split()[1])
					print "cols: "+str(cols)
	elevation=np.fromfile(bin_name,'>h')
	elevation=np.reshape(elevation,(rows, cols))
	if extent!=None:
		nsize=getelevation(north,south,east,west,rows,cols,extent)
		elevation=elevation[nsize[0]:nsize[1],nsize[2]:nsize[3]]
	else:
		extent=[west,east,south,north]
	print 'Chosed extension:{}'.format(extent)	
	elevation=elevation[::step,::step]
	plt.imshow(elevation,cmap='gist_earth',extent=extent)
	plt.xlabel('Longitude')
	plt.ylabel('Latitude')
	plt.title('Map from binaries')
	plt.savefig('figure_raster.png')
	plt.close()
	
def getelevation(north,south,east,west,rows,cols,extent):
		dx=(north-south)/rows
		dy=(east-west)/cols
		nxmin=abs(int((north-extent[3])/dy))
		nxmax=abs(int((extent[3]-extent[2])/dy))+nxmin
		nymin=abs(int((west-extent[0])/dx))
		nymax=abs(int((extent[1]-extent[0])/dx))+nymin
		nsize=[nxmin,nxmax,nymin,nymax]
		#ndx=(nxmax-nxmin)
		#ndy=(nymax-nymin)
		#ndmax=ndx*ndy
		#ndmin=nxmin+nymin
		#elevation=np.fromfile(bin_name,'>h',count=ndmax)
		return nsize
	