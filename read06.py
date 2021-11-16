import shapefile
sf = shapefile.Reader("soal5.shp")
anu=sf.shapes()
print(anu[0].shapeType)





