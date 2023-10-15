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

# membuat matriks 2 x 2
print("== Matriks 2x2 ==")
var_mat = [[5, 0],
           [1, -2]]

def_mat = [[0 for j in range(2)] for i in range(2)]

# looping dengan dua kondisi
for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j]*2
print(def_mat)


# matriks 2 x 2 menggunakan numpy
var_math = numpy.array([[5, 0],     # tidak perlu menggunakan perulangan default matriks
                        [1, -2]])
res = var_math*2
print(res)
