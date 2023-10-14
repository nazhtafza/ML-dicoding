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

# Implementasi matriks dengan deklarasi dan inisialisasi
matrix = [[1, 0, 1, 0, 1],
          [0, 1, 0, 1, 0],
          [1, 0, 1, 0, 1]]  # insialisasi matriks satuan baris = 3, kolom 5
print(matrix)

# deklarasi matriks default
# range pertama merupakan baris, dan range kedua merupakan kolom
matrix_def = [[0 for j in range(5)] for i in range(3)]
print(matrix_def)

# akses elemen matriks

print("mengakses matrix")
var_mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]

print(var_mat[0][1])  # -> mengakses pada baris/index ke 0 dan kolom ke-1
