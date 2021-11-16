import shapefile
sf = shapefile.Reader("soal9.shp")
dit=sf.shapes(0)
print(len(dit))

