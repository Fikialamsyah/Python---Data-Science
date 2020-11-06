# List
# sifat list :
# 1. list berisi koleksi nilai / data.
# 2. list berisi tipe data apapun dan tidak harus semua data berisi tipe data yg sama.
# 3. List bisa berubah


# membuat list
kelas1 = ['fiki', 19, 'dika', 18, 'rafi', 20]
kelas2 = ['ayu', 19, 'bandi', 20, 'fajar', 20]

# mmembuat list baru dan dicampur dengan 2 list
kampus = [kelas1, kelas2]
print(kampus)

# akses data pada list
print(kelas1[0])
print(kelas2[2])


# Manipulasi List
# mengubah nama mahasiswa
kelas2[0] = 'james'

# menghilangkan element list
del (kelas2[3])

# menggunakan method pada list
# pop
kelas2.pop()

# remove
kelas1.remove('rafi')

# len : mengambil panjang daftar
len(kelas1)

# sorted: mengurutkan elemen pada list
sorted(kelas1)

# sum : menjumlahkan semua elemen pada list
number = [1, 2, 3, 4]
sum(number)

# copy : mengcopy isi pada list
a = [1, 2, 3]
b = a.copy()

# list comprehension : membuat list berdasarkan list yang ada
intList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i for i in number if i > 7]







