# Exercitiul 1:
# declarare si initializare variabile

nume = 'Tapu'
varsta = 27
ore_pentru_invatat = 2.5
invat_python = True

#  Exercitiul 2:
# folosirea functiei (type)

print(type(nume))
print(type(varsta))
print(type(ore_pentru_invatat))
print(type(invat_python))

#  Exercitiul 3:
# functia round si suprascriere

ore_pentru_invatat = round(ore_pentru_invatat)
print(ore_pentru_invatat)
print(type(ore_pentru_invatat))

#  Exercitiul 4:

print(f'Numele meu de familie este {nume}')
print(f'Varsta mea este de {varsta}')
print(f'Eu invat python {ore_pentru_invatat} h/pe zi')
print(invat_python)

#  Exercitiul 5:

nume = input('Introduceti numele ')
prenume = input('Introduceti prenumele ')
caractere = len(nume) + len(prenume)
print(f'Numele complet are {caractere} caractere')

# Exercitiul 6:

lungime = int(input('Introduceti lungimea '))
latime = int(input('Introduceti latimea '))
print(f"Aria triunghiului este {lungime * latime}")

#  Exercitiul 7:

variabila_string = 'Coral is either the stupidest animal or the smartest rock'
print(variabila_string.count('the'))

#  Exercitiul 8:

a = variabila_string.replace('the', 'THE')
print(a)

#  Exercitiul 9:

assert variabila_string.isnumeric() == True, 'Eroare, nu contine numere'
print('Acest string contine numere')

# Exercitiul 10:

x = str(input('Introduceti un string de dimensiune impara '))
print(f'Caracterul din mijloc a variabilei de tip string {x} este {x[(len(x) // 2)]}')

# Exercitiul 11:

x = input('Introduceti un string de la tastatura ')
y = x[::-1]
assert x == y, 'Eroare: nu este palindrom'
print('Stringul este palindrom')

# Exercitiul 12:

x = input('Introduceti un string de la tastatura '); cuvant1, cuvant2 = x.split(); print(cuvant1); print(cuvant2)

# Exercitiul 13:

a = input('Introduceti un string de la tastatura ')
primul_caracter_variabila = a[0]
print(primul_caracter_variabila)
ab = a.replace('a', 'A')
abc = ab[1:len(ab)-1]
abc1 = ab[0].lower() + abc + ab[len(ab)-1].lower()
print(abc1)

# Exercitiul 14:

user = input('Introduceti un user ')
password = input('Introduceti o parola ')
lungime = str(len(password))
password1 = password.replace(password, '*' * len(password))

print(f"Parola pentru {user} este {password1} si are {lungime} caractere")
