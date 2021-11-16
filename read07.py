import shapefile
sf = shapefile.Reader("soal9.shp")
anu=sf.shapes()
print(anu[1].parts)
