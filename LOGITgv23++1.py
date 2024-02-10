# from random import *
# nimed=["Kadri","Mirje","Maadis","Kadri","Kadri"]
# while True:
#     v=input("N-andmeta näitamine\n").upper()
#     if v=="N":
#         v==input("Kas köik(k) või Juhuslik nimi?(j)").lower()
#         if v=="k":
#             print(nimed)
#         elif v=="j":
#             print(choice(nimed))
            
#2
# from random import *
# nimed=["Kadri","Mirje","Maadis","Kadri","Kadri"]
# while True:
#     print("------------------")
#     v=input("N-andmeta näitamine\nL-andmete lisamine\n").upper()
#     if v=="N":
#         v==input("Kas köik(k) või Juhuslik nimi?(j)").lower()
#         if v=="k":
#             print(nimed)
#         elif v=="j":
#             print(choice(nimed))
#     elif v=="l":
#         v==input("Kas lõppu?(l) või positsiooniile?(p)").lower()
        
#             nimi=input("Sisesta nimi: ")
#             nimed.append(nimi)
#    
#    
#             `
#1
 
# from string import *
# vokaali=["a","u","i","o","e","ü","ä","õ","ö","y"]
# konsonanti="qwrtpsdfghklzxcvbnmj"
# märgid=punctuation
# v=k=m=t=0
# tekst=input("Sisesta tekst: ")
# print(tekst)
# tekst_list=list(tekst)
# print(tekst_list)
# for element in tekst_list:
#     if element.lower() in vokaali:
#         v+=1
#     elif element.lower() in konsonanti:
#         k+=1
#     elif element in märgid:
#         m+=1
#     elif element==" ":
#         t+=1
        
# print("Vokaali:",v)
# print("Konsonanti:",k)
# print("Märgid:",m)


2
nimed = []
for i in range(5):
    nimi = input("Sisesta nimi: ")
    nimed.append(nimi)
print("Sisestatud: ",nimed)
nimed.sort()
print("Sorteeritud: ",nimed)
print("Vimasena oli lisatud:", nimed)
nimi=str(input("Mis nimi on vaja asendada? "))#!!!kodus
indeks=nimed.indeks(nimi)
uus_nimi=input("Uus nimi: ")
nimed[indeks]=uus_nimi
nimed=[uus_nimi if vana_nimi==nimi else vana_nimi for vana_nimi in nimed]
nimed=list(set(nimed))#!!!kodus
print(nimed)
# vanused = []
# for i in range(5):
#     nimi = input("Sisesta nimi: ")
#     nimed.append(nimi)
# print("Sisestatud: ",nimed)
# sum_=sum(vanused)
# min_=min(vanused)
# max_=max(vanused)
# kesk=sum_/len(vanused)
# print("Kesknime on {kesk}, \nSuurim on {max_}, \nVäiksem on {min_}, \nSumma on {sum_}")


#1

# nimed = []
# for i in range(5):
#     nimi = input("Sisesta nimi: ")
#     nimed.append(nimi)
#     nimed.sort()
# print("Nimed tähestikulises järjekorras:", nimed)
# viimane_lisatud_nimi = nimed[-1]
# print("Viimati lisatud nimi on:", viimane_lisatud_nimi)
# print("Muudame nime 'Juhan' nimeks 'Jaanus':")
# if 'Juhan' in nimed:
#     nimed[nimed.index('Juhan')] = 'Jaanus'
# print("Uus nimede loend:", nimed)
# opilased = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati']
# unikaalsed_nimed = list(set(opilased))
# print("Unikaalsed nimed opilaste hulgas:", unikaalsed_nimed)
# vanused = [21, 25, 30, 35, 40]
# min_vanus = min(vanused)
# max_vanus = max(vanused)
# kogusumma = sum(vanused)
# keskmine_vanus = kogusumma / len(vanused)

# print("Väikseim vanus:", min_vanus)
# print("Suurim vanus:", max_vanus)
# print("Kogusumma:", kogusumma)
# print("Keskmine vanus:", keskmine_vanus)

#2

import random

print("Tere tulemast matemaatika testi!")

raskused = int(input("Valige raskusaste (1, 2 või 3): "))
num_küsimused = int(input("Mitu ülesannet soovite lahendada? "))
õiged_vastused = 0

for _ in range(num_küsimused):
    operatsioonid = ['+', '-', '*', '/', '**']
    operatsiooni = random.valik(operatsioonid[:raskused])
    num1 = random.randint(1, 10 ** raskused)
    num2 = random.randint(1, 10 ** raskused)

    if operatsiooni == '/':
        while num1 % num2 != 0: 
            num1 = random.randint(1, 10 ** raskused)
            num2 = random.randint(1, 10 ** raskused)

    küsimus = (f"Mis on {num1} {operatsiooni} {num2}? ")
    vastus = float(input(küsimus))

    if operatsiooni == '+':
        õige_vastus = num1 + num2
    elif operatsiooni == '-':
        õige_vastus = num1 - num2
    elif operatsiooni == '*':
        õige_vastus = num1 * num2
    elif operatsiooni == '/':
        õige_vastus = num1 / num2
    elif operatsiooni == '**':
        õige_vastus = num1 ** num2

    if abs(vastus - õiged_vastused) < 0.001:  
        print("Õige!")
        õiged_vastused += 1
    else:
        print("Vale.")

tulemus = (õiged_vastused / num_küsimused) * 100
print(f"Sinu tulemus: {tulemus:.2f}%")
if tulemus < 60:
    print("Hinne 2")
elif tulemus < 75:
    print("Hinne 3")
elif tulemus < 90:
    print("Hinne 4")
else:
    print("Hinne 5")
    