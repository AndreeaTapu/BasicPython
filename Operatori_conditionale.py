# Exercitiul 1:

x = int(input('Introduceti numarul '))
if x >= 0 and type(x) == int:
    print('numar natural')
else:
    print('nu este numar natural')

# Exercitiul 2:

x = int(input('Introduceti numarul '))
if x > 0:
    print('numar pozitiv')
elif x == 0:
    print('numar neutru')
elif x < 0:
    print('numar negativ')

# Exercitiul 3:

x = 5
if x >= -2 and x <= 13:
    print('x este in acest interval')
else:
    print('x nu este in acest interval')

# Exercitiul 4:

x = 7
y = 5
if (x - y) < 5:
    print('se indeplineste conditia')
else:
    print('nu se indeplineste conditia')

# Exercitiul 5:

x = 2
if not (x >= 5 and x <= 27):
    print('x este in acest interval')
else:
    print('x nu este in acest interval')

# Exercitiul 6:

x = 8
y = 12

if x == y:
    print('sunt egale')
elif x > y:
    print('x este mai mare decat y')
else:
    print('y este mai mare decat x')


# Exercitiul 7:

x = int(input('Introduceti numarul '))
y = int(input('Introduceti numarul '))
z = int(input('Introduceti numarul '))

if x == y != z or x != y == z or y != x == z:
    print('triunghiul este isoscel')
elif x == y and x == z and y == z:
    print('triungiul este echilateral')
elif x != y != z:
    print('triunghi oarecare')


# Exercitiul 8:

x = input('Scrie o litera de la tastatura ')
vocale = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
if x in vocale:
    print("Este vocala")
else:
    print("Este Consoana")

# Exercitiul 9:

note = int(input('Introduceti nota '))
if note <= 4:
    print('f')
elif note > 4 and note <= 6:
    print('e')
elif note > 6 and note <= 7:
    print('d')
elif note > 7 and note <= 8:
    print('c')
elif note > 8 and note <= 9:
    print('b')
elif note > 9 and note <= 10:
    print('a')
else:
    print('numar mai mare de 10')


# Exercitiul 10:

x = 199535

if len(str(x)) >= 4:
    print('x are min 4 cifre')
else:
    print('x nu are min 4 cifre')

# Exercitiul 11:

if len(str(x)) == 6:
    print('x are exact 6 cifre')
else:
    print('x nu are exact 6 cifre')

# Exercitiul 12:

if x % 2 == 0:
    print('x este numar par')
else:
    print("x este numar impar")


# Exercitiul 13:

x = input('Intruduceti numarul ')
y = input('Intruduceti numarul ')
z = input('Intruduceti numarul ')

print(max(x, y, z))

# Exercitiul 14:

x = int(input('Intruduceti numarul '))
y = int(input('Intruduceti numarul '))
z = int(input('Intruduceti numarul '))

sumnr = x+y+z

if sumnr == 180:
    print('Triunghiul este valid')
else:
    print('Triunghiul nu este valid')

# Exercitiul 15:

variabila_a = "Coral is either the stupidest animal or the smartest rock"
x = int(input('Introdu un numar '))
# print(variabila_a[0:len(variabila_a)-x])
print(variabila_a[:-x])

# Exercitiul 16:

variabila_b = variabila_a[0:5] + variabila_a[-5:]
print(variabila_b)

# Exercitiul 17:

variabila_index = variabila_a.index('rock')
print(variabila_index)
print(variabila_a[0:variabila_index])

# Exercitiul 18:

string_tastatura = input('Introduceti un string ')
assert string_tastatura[0] == string_tastatura[-1], 'Eroare : primul și ultimul caracter nu sunt la fel'
print('Primul și ultimul caracter sunt la fel')

# Exercitiul 19:

string_x = '0123456789'

print(string_x[::2])         # se afiseaza numere pare
print(string_x[1::2])        # se afiseaza numere impare

# Exercitiul 20:

from random import randint

dice_roll = randint(1, 6)

numar_ghicit_utilizator = int(input('Ghiciti numarul de pe zaruri '))

if numar_ghicit_utilizator < dice_roll:
    print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_ghicit_utilizator} si zarul a fost {dice_roll}.")
elif numar_ghicit_utilizator > dice_roll:
    print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ghicit_utilizator} si zarul a fost {dice_roll}.")
else:
    print(f"Ai ghicit. Felicitari! Ai ales {numar_ghicit_utilizator} si zarul a fost {dice_roll}.")
