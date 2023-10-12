# len() -> menghitung panjang elemen dari list, set, string
egList = [1, 2, 3, 4, 5, 6, 7]
print(egList)

print(len(egList))

# set() -> menghitung jumlah angka
setList = set([1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 9])
print(setList)
print(len(setList))

# String -> menghitung jumlah kalimat
stringList = "Sinawu Python"
print(stringList)
print(len(stringList))

# min() dan max()
number = [13, 45, 7, 23, 35, 90]
print(min(number))
print(max(number))

# count -> untuk mengetahui angka yang muncul beberapa kali
genap = [2, 4, 4, 4, 4, 6, 6, 8, 8, 10]
print(genap.count(4))

kalimat = "nazhat belajar piton dan sangat senang"
substring = "a"
print(kalimat.count(substring))

# In dan Not In -> mengetahui nilai atau objek yang ada dalam list
word = "sinau piton di dicoding menyenangkan"
print('piton' in word)
