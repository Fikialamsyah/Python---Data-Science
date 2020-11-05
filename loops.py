# for loop

# looping dengan mengambil dari range()
for i in range(5):
    print(i)

# looping dari list
mahasiswa = ['Fiki', 'Di5ka', 'Rafi', 'Bandi']
for name in mahasiswa:
    print(name)

# looping dengan menggunakan enumerates()
numbers = [1, 2, 3, 4, 5]

for index, number in enumerate(numbers):
    print(f'index: {index} value : {number}')

# while loop
i = 0
while (i < 10):
    print(i)
    i += 1

while True:
    a = input('Masukan kata : ')
    if a == 'quit':
        break
    print(f'panjanag kata : {len(a)}')
