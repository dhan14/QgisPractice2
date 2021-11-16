import shapefile
sf = shapefile.Reader("soal5.shp")
print(sf.shapeType)


"""""
apakah keluaran dari script tersebut dan cocokkan dengan daftar berikut :
- NULL = 0
- POINT = 1
- POLYLINE = 3
- POLYGON = 5
- MULTIPOINT = 8
- POINTZ = 11
- POLYLINEZ = 13
- POLYGONZ = 15
- MULTIPOINTZ = 18
- POINTM = 21
- POLYLINEM = 23
- POLYGONM = 25
- MULTIPOINTM = 28
- MULTIPATCH = 31

Tunjukkan hasilnya dan jelaskan perbaris diatas
"""

