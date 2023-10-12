# Transformasi angka, karakter, dan string

# Uppercase -> membuat karakter menjadi kapital semua (uppercase)
word = 'ingfo ngoding'
word = word.upper()
print(word)

# Lowecase -> membuat karakter menjadi huruf kecil
kata = 'MALING'
kata = kata.lower()
print(kata)

# Awalan dan akhiran

# rstrip -> untuk menghapus whitespace pada sebelah kanan atau akhiran
print("dicoding             ".rstrip())

# lstrip -> untuk menghapus whitespace pada sebelah kiri atau awalan
print("     dikocok".lstrip())

# strip -> menghaspus whitespace yang ada di sebelah kanan dan kiri
kalimat = ("jatjatNasajatjatjat")
print(kalimat.strip("jat"))

# startswith() -> menemukan kata pada awalan string
print("nazhat ganteng".startswith("nazhat"))

# endswith() -> menemukan pada akhir string
print("nazhat jlek".endswith("nazhat"))

# Memisah dan menggabung string
# join
print(' '.join(['Dicoding', 'Indonesia', '!']))

# join menggunakna delimiter
print('123'.join(['Dicoding', 'Indonesia', '!']))

# split -> memisahkan kata atau substring berdasarkan delimeter
print('Dicoding Indonesia !'.split())

# split multiline
print('''Halo, 
      Aku Nazhat,
      Aku berumur 19,
      salam kenal'''.split())


# Mengganti elemen string

# replace() -> mengganti elemen string menggunakan elemen string lainnya
belajar = 'ayo belajar ngising'
print(belajar.replace('ngising', 'ngoding'))

# Pengecekkan string

# isupper() -> akan menghasilkan kata True apabila string menggunakan uppercase,
# apabila salah maka akan mengembalikan nilai False.

course = "UMK"
print(f"menggunakan huruf kapital = {course.isupper()}")

learn = "machine learning"
print(f"menggunakan huruf kapital = {learn.isupper()}")

# islower() -> menghasilkan kata True jika string menggunakan lowercase,
# apabila salah maka akan mengembalikan nilai false

truemint = "riil cuy"
print(f"kata ini lowercase = {truemint.islower()}")

falsemint = "FALSE LUR"
print(f"kata ini lowercase = {falsemint.islower()}")

# isalpha() -> menghasilkan kata true apabila sebuah kata menggunakan alfabet
# apabila salah satu terdapat bukan alfabet, maka menghasilkan nilai false

alfabet = 'hari'
print(f"kata hari ini adalah semua alfabet = {alfabet.isalpha()}")

alfa = 'hari ke1'
print(f"kata hari ini adalah semua alfabet = {alfabet.isalpha()}")

# isalnum() -> menghasilakan kata true apabila sebuah kata menggunakan alfanumerik,
# apabila tidak alfanumerik maka menghasilkan false

alfanumerik = 'admin123'
print(f"admin123 merupakan alfanumerik = {alfanumerik.isalnum()}")

fixfalse = '@'
print(f"@ merupakan kata alfanumerik = {fixfalse.isalnum()}")

# isdecimal() -> dalam sebuah kata hanya menggunakan numerik atau angka

print('123'.isdecimal())

# isspace() -> dalam sebuah string hanya terdapat space
print(' '.isspace())

# istitle() -> dalam kata dalam sebuah string menggunakan awalan kapital
print('Nazhat'.istitle())

# Formatting dalam string

# zfill() -> menambahkan nilai 0 (nol) didepan sebuah string.
textBolo = 'Codes'
tambah_number = textBolo.zfill(7)
print(tambah_number)

# rjust() -> merapikan percetakan teks, lebih rapi
print('dicoding'.rjust(10))

# kita dapat menambahkan teks ataupun simbol pada space
print('dicoding'.rjust(20, '!'))

# ljust() -> mengubah string menjadi rata kiri
print('dicoding'.ljust(10))

# center -> mengubah string menjadi rata tengah
print('dicoding'.center(10, '-'))

# String literals -> apabila 'jum'at' error karena dapat menutup quote
st1 = "Jum'at"
print(st1)

print("halo semua! \n aku Nzhat")

# Raw String -> mencetak string sesuai apa yang dituliskan
print(r"halo aku \t nasa")
