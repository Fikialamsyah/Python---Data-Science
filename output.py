# cetak sebuah string
name = 'Fiki'
age = 19

# menggunakan (+)
print('Hello i am ' + name + 'and i am ' + str(age) + ' years old')
# menggunakan (-)
print('Hello i am', name, 'and i am', age, 'years old')

# String Formating

# Old Style
print('Hello i am %s and i am %d years old' % (name, age))

# New Style
print('Hello i am {0} and i am {1} years old'.format(name, age))

# String Interpolation
print(f'Hello i am {name} and i am {age} years old')