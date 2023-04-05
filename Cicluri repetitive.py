# Exercitiul 1:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for i in range(len(masini)):
    print(f"Masina mea preferata este {masini[i]}")
print('--------FOR--------')

for masina in masini:
    print(f"Masina mea preferata este: {masina}")
print('--------FOR EACH--------')

s = 0
while s in range(len(masini)):
    print(f"Masina mea preferata este: {masini[s]}")
    s += 1
print('--------WHILE--------')

# Exercitiul 2:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for x in masini[1:-1]:
    index = masini.index(x)
    masini[index] = x.upper()
print(masini)

# Exercitiul 3:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masina_dorita_de_cumparator = 'Mercedes'
for i in range(len(masini)):
    if masini[i] == masina_dorita_de_cumparator:
        print("Am gasit masina dorita de dumneavoastra.")
        break
    else:
        print(f"Am gasit masina: {masini[i]}. Mai cautam.")

# Exercitiul 4:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Lăstun' or masina == 'Trabant':
                continue
    print(f"S-ar putea să vă placă mașina: {masina}")

# Exercitiul 5:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for masina in masini:
    if masina == 'Lăstun' or masina == 'Trabant':
        masini_vechi.append(masina)
        masini[masini.index(masina)] = 'Tesla'
print(f'Modele noi: {masini}')
print(f'Modele vechi: {masini_vechi}')

# Exercitiul 6:

pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

for key in pret_masini.keys():
    if pret_masini.get(key) < 15000:
        print(f"Pentru un buget de 15000 euro puteti alege masina {key} la pretul de {pret_masini[key]}")

# Exercitiul 7:

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count = 0
for numar in numere:
    if numar == 3:
        count += 1
print(f"Numarul 3 apare de {count} ori in lista")

# Exercitiul 8:

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for i in range(len(numere)):
    suma = suma + numere[i]
print(f"Suma numerelor din lista este: {suma}")

# Exercitiul 9:

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max = 0
for numar in numere:
    if numar > max:
        max = numar
print(f"Cel mai mare numar din lista este: {max}")

# Exercitiul 10:

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)

# Exercitiul 11:

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    elif numar % 2 != 0:
        numere_impare.append(numar)

    if numar >= 0:
        numere_pozitive.append(numar)
    elif numar < 0:
        numere_negative.append(numar)
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

# Exercitiul 12:

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
temp = 0
for i in range(0, len(alte_numere)):
    for j in range(i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            temp = alte_numere[i]
            alte_numere[i] = alte_numere[j]
            alte_numere[j] = temp
print(alte_numere)

# Exercitiul 13:

import random
numar_secret = random.randint(1, 30)
numar_ghicit = None
print(numar_secret)
while True:
    numar_ghicit_user = int(input("Introduceti un numar "))
    if numar_secret > numar_ghicit_user:
        print("Nr secret e mai mare")
    elif numar_secret < numar_ghicit_user:
        print("Nr secret e mai mic")
    elif numar_secret == numar_ghicit_user:
        print("Felicitari! Ai ghicit!")
        break

# Exercitiul 14:

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")

# Exercitiul 15:

tastatura_telefon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

for i in range(len(tastatura_telefon)):
  for j in range(len(tastatura_telefon[i])):
    print(f"Cifra curentă este : {tastatura_telefon[i][j]}")
