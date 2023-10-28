import json

# membuat json
x = '{"nama": "nasa", "umur": "19", "kota": "kudus"}'

# parse json
y = json.loads(x)

# tampilkan
print(y["umur"])

# file tidak boleh sama dengan package
