import shapefile
sf = shapefile.Reader("soal5.shp")
print(sf.bbox)