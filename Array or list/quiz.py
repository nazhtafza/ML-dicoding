var_array = [i for i in range(101)]
print(var_array)
total = 0

# menambahkan semua nilai dalam list
for num in var_array:
    total += num

print(total)

# menghitung rata-rata

average = total/len(var_array)
print(average)
