# Fungsi : merupakan sebuah sebuah sub program sehingga bisa dipanggil berulang kali

# mendefinisikan fungsi (def)
def sayHello():
    print('Hello')


# fungsi dengan argument
def sayHello(name):
    print('Hello', name)


# fungsi dengan default argument
def sayHello(name='Fiki'):
    print('Hello', name)


# fungsi lambda : anonim function
f = lambda x: x**x


# cara memanggil fungsi
sayHello('fiki')
f(2)


