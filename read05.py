import shapefile
sf = shapefile.Reader("soal9.shp")
anu=sf.shapes()
print(dir(anu))
#print("------------batasan------------")
print(dir(anu[0]))

