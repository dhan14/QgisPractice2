import shapefile
sf = shapefile.Reader("practice9/soal9.shp")
isidata = sf.records()
print(isidata[1])