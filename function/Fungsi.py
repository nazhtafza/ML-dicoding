# create direktori and then import function
from funct_lingkaran import lingkaran, kel_lingkaran
from funt_triangle import l_segitiga
# contoh user defined function


def rectangle(panjang, lebar):
    luas_rectangle = panjang*lebar
    return luas_rectangle


rectangle1 = rectangle(10, 5)
print(f" luas persegi panjang 1 {rectangle1}")

rectangle2 = rectangle(20, 2)
print(f" luas persegi panjang 2 {rectangle2}")

# print result luas lingkaran
lingkaran1 = lingkaran(30)
print(f"luas lingkaran adalah: {lingkaran1}")

lingkaran_kel = kel_lingkaran(30)
print(f"keliling lingkaran: {lingkaran_kel}")

# luas segitiga

print(f"hasil luas segitiga {l_segitiga(20, 10)}")
