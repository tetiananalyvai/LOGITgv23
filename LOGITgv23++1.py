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


#2
# nimed = []
# for i in range(5):
#     nimi = input("Sisesta nimi: ")
#     nimed.append(nimi)
# print("Sisestatud: ",nimed)
# nimed.sort()
# print("Sorteeritud: ",nimed)
# print("Vimasena oli lisatud:", nimed)
# nimi=input("Mis nimi on vaja asendada? ")#!!!kodus
# indeks=nimed.indeks(nimi)
# uus_nimi=input("Uus nimi: ")
# nimed[indeks]=uus_nimi
# nimed=[uus_nimi if vana_nimi==nimi else vana_nimi for vana_nimi in nimed]
# nimed=set(nimed)#!!!kodus
# print(nimed)
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