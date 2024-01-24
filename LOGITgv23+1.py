
from datetime import *
from random import *

arve_nr= date.today()#datetime.now()
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0

tooded=["Piim","Leib","Kommid"]
for i in range(len(tooded)):
    toode=tooded[i]
    hind=randint(50,150)/100
    v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahat osta?").lower()
    if v=="jah":
        mitu=int(input("Mitu"))
        tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
        summa+=mitu*hind
        
tsekk+="Kokku maksta: "+str(summa)
print(tsekk)


#Ülesanne 1
# nimi=input("Palun sisesta oma nimi:")
# mitu=int(input("Mitu korda tervitada? "))
# for i in range(mitu):
#     print(f"Oletervitatud, {nimi}, {i+1}. korda.")
    
#Ulesanne 2
# for i in range(10):
#     arv=int(input("Sisesta arv: "))
#     sum_+=arv
# print("Summa= {sum_}")

#Ulesanne 2.1
# sum_=0
# i=0
# while True:
#     i+=1
#     arv=int(input("Sisesta arv: "))
#     if i i>10: break 
#     if arv==777: break 
#     sum_+=arv
# print(f"Summa= {sum_}")

#Ulesanne 2.2 sone "q" lopeb tsukkel
# sum_=0
# i=0
# while True:
#     i+=1
#     arv=input("2.2 Sisesta arv: ")
#     if i>10: break 
#     try:
#         arv=int(arv)
#         sum_+=arv
#     except:
#         break 
# if sum_!=0:
#     print(f"Summa= {sum_}")
    
#Ulesanne 3
# k=0
# while True:
#     k+=1
#     print(f"{k}. ülesanne")
#     a=randint(1,50)
#     b=randint(1,50)
#     p=5
#     while True:
#         v=int(input(f"{a}+{b}= "))
#         p-=1
#         if v==a+b:
#             print("Õige vastus!")
#             break 
#         elif p==0:
#             print(f"{a}+{b}={a+b}")
#             break 
#         if k==10: break

#Ulesanne 4

# for i in range(1,11):
#     for j in range(1,11):
         
#          print(f"{i}*{j}={i*j}")

#Ulesanne 5
# for i in range(1,11):
#     for j in range(1,11): 
#         print(f"0",end="")
#     print()
    