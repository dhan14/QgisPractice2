
import shapefile
sf = shapefile.Reader("soal1.shp")
anu=sf.shapes()
print(anu[0].points)
print('pemisah')
print(anu[1].points)

