import numpy
import sys
matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriks)

# perbandingan list dan numpy
var_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(
    f"ukuran elemen list dalam byte: {sys.getsizeof(var_list)*len(var_list)} bytes")
print(
    f"ukuran elemen array using numpy dalam byte: {var_array.size*var_array.itemsize}")
