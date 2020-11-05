# Exception Handling
# Try : suatu statemen yg mengatasi kode error
# Except : suatu statemen yg menghandle apabila ada error
# finally : suatu statement yg mengakses suatu kode

number1 = int(input('Masukan angka pertama : '))
number2 = int(input('Masukan angka kedua   : '))

try:
    hasil = number1/number2
    print(f'hasil : {number1} / {number2} = {hasil}')
except Exception as e:
    print(f'Error : {e}')
finally:
    print('Finish') # akan di eksekusi baik error atau tidak