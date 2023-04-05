# Exercitiul 1:

def suma_doua_numere(nr_1, nr_2):
    suma = nr_1 + nr_2
    print(f"Suma celor doua numere este: {suma}")

suma_doua_numere(15, 56)

# Exercitiul 2:

x = int(input('Introduceti un numar '))

def numar_par_sau_numar_impar(x):

    if x % 2 == 0:
        print(x, "Numarul este par")
    else:
        print(x, "Numarul este impar")

numar_par_sau_numar_impar(x)

# Exercitiul 3:

def len_nume_prenume(nume, prenume):
    return len(nume + prenume)

print(len_nume_prenume('Tapu', 'Andreea'))

# Exercitiul 4:

def aria_dreptunghiului (lungime, latime):
    aria = lungime * latime
    print(f"Aria dreptunghiului este: {aria} cm")
lungime = int(input("Introduceti lungimea "))
latime = int(input("Introduceti latimea "))
aria_dreptunghiului(lungime, latime)

# Exercitiul 5:

import math

def aria_cercului (raza):
    aria_c = raza ** 2 * math.pi
    return aria_c

raza = int(input("Introduceti raza cercului "))
print("Aria cercului este:", aria_cercului(raza), "cm")

# Exercitiul 6:

def caracter_intr_un_string_dat (string, x):
    if x in string:
        return True
    else:
        return False

print(caracter_intr_un_string_dat("mamaliga", "m"))

# Exercitiul 7:

def caractere_lower_upper(string_caractere):
    caractere_lower = 0
    caractere_upper = 0
    for caracter in string_caractere:
        if caracter.islower():
            caractere_lower += 1
        elif caracter.isupper():
            caractere_upper += 1
    print(f'Numarul de caractere lower: {caractere_lower}')
    print(f'Numarul de caractere upper: {caractere_upper}')

caractere_lower_upper("abcDEFmnoFVis")

# Exercitiul 8:

def numere_pozitive(lista_numere):
    lista_numere_pozitive = []
    for numar in lista_numere:
        if numar > 0:
            lista_numere_pozitive.append(numar)
    return lista_numere_pozitive

lista_numere = [1, 5, 8, -8, -9, 0, -10, 5, 6, -2, 2, 2]
print(f"Lista numerelor pozitive este: {numere_pozitive(lista_numere)}")

# Exercitiul 9:

def numere_de_comparat(nr_1, nr_2):
    if nr_1 > nr_2:
        print(f"Primul numar {nr_1} este mai mare decat al doilea numar {nr_2}")
    elif nr_1 < nr_2:
        print(f"Al doilea numar {nr_2} este mai mare decat primul numar {nr_1}")
    else:
        print("Numerele sunt egale")

numere_de_comparat(17, 15)

# Exercitiul 10:

def numar_set_numere(nr, set):
    if nr in set:
        print(f"Nu am adaugat numărul {nr} în set. Acesta există deja")
        return False
    else:
        set.add(nr)
        print(f"Am adaugat numărul nou {nr} în set’")
        return True

set = {7, 0, 2, -6, 8, 5, 1}
numar_set_numere(2, set)


# Exercitiul 11:

from calendar import monthrange

def numere_zile_in_luna(an, luna):
    return monthrange(an, luna)[1]

print(numere_zile_in_luna(2022, 8))

# Exercitiul 12:

def functie_calculator(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d

a, b, c, d = functie_calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

# Exercitiul 13:

def frecventa_numarare_lista_de_cifre(lista):
    dictionar_gol = {}
    for i in [1, 1, 2, 2, 2, 5, 6, 8, 9, 5, 8, 7, 7, 0, 6, 9, 9, 8]:
        dictionar_gol[i] = dictionar_gol.get(i, 0) + 1
    return dictionar_gol

if __name__ == "__main__":
    lista = [1, 1, 2, 2, 2, 5, 6, 8, 9, 5, 8, 7, 7, 0, 6, 9, 9, 8]
    print(frecventa_numarare_lista_de_cifre(lista))

# Exercitiul 14:

def maxim_doua_numere( x, y ):
    if x > y:
        return x
    return y
def maxim_trei_numere(x, y, z):
    return maxim_doua_numere(x, maxim_doua_numere(y, z))

print(maxim_trei_numere(7, 21, 13))
