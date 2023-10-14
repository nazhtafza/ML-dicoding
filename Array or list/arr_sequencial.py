# mendefinisikan sebuah variable dari list
var_arr = [1, 2, 3, 4, 5]

# membuat program menggunakan looping
for i in range(len(var_arr)):
    elemen_kini = var_arr[i]  # indexing method
    index_lanjut = i + 1  # index successor

    if index_lanjut < len(var_arr):
        elemen_lanjut = var_arr[index_lanjut]
    else:
        elemen_lanjut = None

    print(
        f"elemen terikin: {elemen_kini}, elemen selanjutnya: {elemen_lanjut}")

# mencari nilai terbesar dalam array
# two pointer method
array = [1, 7, 2, 89, 3]
pointer_kiri = array[0]  # define left pointer is index 0

# find max value using loop
for i in range(len(array)):
    pointer_kanan = array[i]
    if pointer_kanan > pointer_kiri:
        pointer_kiri = pointer_kanan

print(f"result of lef pointer {pointer_kiri}")
