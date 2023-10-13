# jika ingin menggunakan array harus meng-import array terlebih dahulu
import array

# list
x = [1, 2, 3, 4]
print(x)

# array
x = array.array("i", [1, 2, 3, 4, 5])
print(x)
print(type(x))

# index dimulai dari 0
siswa = [10, 100, 50, 85, 90, 40]
print(siswa)

# mengambil index ke - 0
print(siswa[0])

# elemen -> menghasilkan lokasi memori setiap elemen pada list
var_list = [1, 2, 3]
for elemen in var_list:
    print(id(elemen))

# define array value
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(var_arr)

# define default value
name_var = [0 for i in range(10)]
print(name_var)

# change default with new value
for i in range(10):
    name_var[i] = i
print(name_var)

print(name_var[0])
