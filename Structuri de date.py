# Exercitiul 1:

note_muzicale = ['do', 're', 'mi','fa','sol', 'la', 'si', 'do']
print(f'Lista notelor muzicale este: {note_muzicale}')

note_muzicale = (['do', 're', 'mi','fa','sol', 'la', 'si', 'do'][::-1])
print(f'Lista notelor muzicale inversata cu slicing si suprascriere  este: {note_muzicale}')

note_muzicale.reverse()
print(f'Lista notelor muzicale inversata cu reverse este: {note_muzicale}')

# Exercitiul 2:

print(f"Nota muzicala do apare in liste de {note_muzicale.count('do')} ori")

# Exercitiul 3:

lista_unu = [3, 1, 0, 2]
lista_doi = [6, 5, 4]

lista_unu.extend(lista_doi)            # metoda 1
print(lista_unu)

lista_trei = lista_unu + lista_doi     # metoda 2
print(lista_trei)

# Exercitiul 4:

lista_trei.sort()
print(lista_trei)

lista_trei.remove(0)
print(lista_trei)

# Exercitiul 5:

if lista_trei == []:
    print('Lista este goală.')
else:
    print('Lista nu este goală.')

# Exercitiul 6:

lista_trei.clear()
print(lista_trei)

# Exercitiul 7:

if lista_trei == []:
    print('Lista este goală.')
else:
    print('Lista nu este goală.')

# Exercitiul 8:

dict1_elevi = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
print(f'Numele elevilor din lista sunt: {dict1_elevi.keys()}')

# Exercitiul 9:

print(f"Ana a luat nota: {dict1_elevi['Ana']}")
print(f"Gigel a luat nota: {dict1_elevi['Gigel']}")
print(f"Dorel a luat nota: {dict1_elevi['Dorel']}")

# Exercitiul 10:

dict1_elevi.update({'Dorel': '6'})
print(f"Noua nota a lui Dorel este: {dict1_elevi.get('Dorel')}")
print(f"Noua nota a lui Dorel este: {dict1_elevi['Dorel']}")

# Exercitiul 11:

dict1_elevi.pop('Gigel')
dict1_elevi['Ionica']=9
print(f'Elevii dupa actualizare sunt: {dict1_elevi}')

# Exercitiul 12:

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
print(zile_sapt)
zile_sapt.add('luni')
print(zile_sapt)  # nu am primit eroare dar nici nu a fost adaugata la set pentru ca ziua de luni era deja mentionata

# Exercitiul 13:

if weekend.issubset(zile_sapt) == True:
    print('Weekend este un subset al zilelor saptamanii')
else:
    print('Weekend nu este un subset al zilelor saptamanii')

# Exercitiul 14:

print(f"Diferenta intre zile_sapt si weekend este : {zile_sapt.difference(weekend)}")

# Exercitiul 15:

print(f"Intersectia dintre cele 2 seturi este {zile_sapt.intersection(weekend)}")
print(f"Intersectia dintre cele 2 seturi este {weekend.intersection(zile_sapt)}")

# Exercitiul 16:

lista_jucatori = ["j1", "j2", "j3", "j4", "j5"]
jucatori_scosi_de_pe_teren = []
lista_rezerve = ["j6", "j7", "j8"]
SCHIMBARI_MAX = 3
nr_schimbari_efectuate = 0  # 2
while nr_schimbari_efectuate < SCHIMBARI_MAX:
    jucator_care_iese = input("introduceti jucatorul care iese")
    jucator_care_intra = input("introduceti jucatorul care intra")
    if jucator_care_iese in lista_jucatori and jucator_care_intra in lista_rezerve:
        print(f"A intrat {jucator_care_intra} si a iesit {jucator_care_iese}")
        lista_jucatori.remove(jucator_care_iese)
        lista_rezerve.remove(jucator_care_intra)
        lista_jucatori.append(jucator_care_intra)
        jucatori_scosi_de_pe_teren.append(jucator_care_iese)
        nr_schimbari_efectuate += 1
        print(f"Mai aveti: {SCHIMBARI_MAX-nr_schimbari_efectuate} schimbari")
    elif jucator_care_iese not in lista_jucatori:
        print(f"Nu se poate efectua schimbarea deoarece jucătorul {jucator_care_iese} nu e în teren")
        print(f"Mai aveti: {SCHIMBARI_MAX - nr_schimbari_efectuate} schimbari")
    else:
        print(f"Nu se poate efectua schimbarea deoarece jucătorul {jucator_care_intra} nu e în lista de rezerve")

print(f"Jucatorii de pe teren la final de meci sunt: {lista_jucatori}")
print(f"Jucatorii care au fost scosi din teren sunt: {jucatori_scosi_de_pe_teren}")
print(f"Lista de rezerve la final de meci este: {lista_rezerve}")
