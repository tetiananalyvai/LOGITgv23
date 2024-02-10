#1
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



#2 list
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