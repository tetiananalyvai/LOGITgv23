
# from datetime import *
# from random import *

# arve_nr= date.today()#datetime.now()
# tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
# summa=0

# tooded=["Piim","Leib","Kommid"]
# for i in range(len(tooded)):
#     toode=tooded[i]
#     hind=randint(50,150)/100
#     v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahat osta?").lower()
#     if v=="jah":
#         mitu=int(input("Mitu"))
#         tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
#         summa+=mitu*hind
        
# tsekk+="Kokku maksta: "+str(summa)
# print(tsekk)


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

# print("*** ИГРЫ С ЧИСЛАМИ ***")
# print()
# #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# while 1:
#     try:
#         a = abs(int(input("Введите целое число => ")))
#         break
#     except ValueError:
#         print("Это не целое число")
# #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# if a==0:
#     print("Нет смысла ничего делать с нулём")
# else:
# #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#     print("Определяем, сколько в числе чётных и сколько нечётных цифр")
#     print()
#     c=a
#     b=a
#     paaris=0
#     paaritu=0
#     while b>0:
#         if b%2==0:
#             paaris=+1    
#         else:
#             paaritu=+1
#         b=b//10
    
#     print("Чётных цифр:" +str(paaris))
#     print("Нечётных цифр:" +str(paaritu))
#     print()
# #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#     print("*Переворачиваем* введённое число")
#     print()
#     b=0
#     while a>0:
#         number=a%10
#         a=a//10
#         b=b*10
#         b+=number
#     print("*Перевёрнутое* число", b)
#     print()
# #''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#     print("Проверяем гипотезу Сиракуз")
#     print()
#     if c%2==0:
#         print(f"{c} - чётное число. Делим на 2.")
#     else:
#         print(f"{c} - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
#     while c!=1:
#             if c%2==0:
#                  c=c/2
#             else:
#                  c=(3*c+1)/2
#             print(c, end="\t")
#     print()
#     print("Гипотеза верна")

        