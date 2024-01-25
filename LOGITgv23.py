
length = float(input("Введите длину комнаты в метрах: "))
width = float(input("Введите ширину комнаты в метрах: "))
floor_area = length * width
print(f"Площадь пола комнаты: {floor_area} кв. м.")

repair_choice = input("Хотите ли вы сделать ремонт (да/нет)? ").lower()
if repair_choice == "да":
    cost_per_square_meter = float(input("Введите стоимость за квадратный метр пола: "))
    total_cost = floor_area * cost_per_square_meter
    print(f"Общая стоимость замены пола: {total_cost} евро.")
else:
    print("Спасибо за ответ. Удачного дня!")
4

original_price = float(input("Введите первоначальную цену компьютера в евро: "))
discount_rate = 0.3  # 30% скидка

if original_price > 700:
    discounted_price = original_price * (1 - discount_rate)
    print(f"Цена со скидкой: {discounted_price} евро.")
else:
    print(f"Цена без скидки: {original_price} евро.")

#5

temperatuur = float(input("Sisesta temperatuur kraadides: "))# Küsi temperatuur kasutajalt

def check_temperature(temp):# Funktsioon temperatuuri kontrollimiseks
    if temp > 18:
        return "Temperatuur on üle 18 kraadi, soovitav toasoojus talvel."
    else:
        return "Temperatuur on 18 kraadi või alla selle, võib olla jahe talvel."

print(check_temperature(temperatuur))# Kutsume välja funktsiooni ja prindime tulemuse

#6

pikkus = float(input("Sisesta inimese pikkus meetrites: "))

luhike_pikkus = 1.50
pikk_pikkus = 1.70
if pikkus < luhike_pikkus:
    print("Inimene on lühike.")
elif luhike_pikkus <= pikkus <= pikk_pikkus:
    print("Inimene on keskmise pikkusega.")
else:
    print("Inimene on pikk.")

#7
pikkus = float(input("Sisesta inimese pikkus meetrites: "))
sugu = input("Sisesta inimese sugu (mees/naine): ").lower()
luhike_pikkus = 1.60
keskmine_pikkus_mees = 1.75
pikk_pikkus_mees = 1.90
keskmine_pikkus_naine = 1.65
pikk_pikkus_naine = 1.80

if sugu == "mees":
    if pikkus < luhike_pikkus:
        print("Mees on lühike.")
    elif luhike_pikkus <= pikkus <= keskmine_pikkus_mees:
        print("Mees on keskmise pikkusega.")
    else:
        print("Mees on pikk.")
elif sugu == "naine":
    if pikkus < luhike_pikkus:
        print("Naine on lühike.")
    elif luhike_pikkus <= pikkus <= keskmine_pikkus_naine:
        print("Naine on keskmise pikkusega.")
    else:
        print("Naine on pikk.")
else:
    print("Sugu ei ole määratud korrektselt.")

#8

import random

tooted = ["piim", "saia", "leiba", "juust", "vorst"]
hinnad = {toode: round(random.uniform(1, 3), 2) for toode in tooted}

ostukorv = {}

print("Poes saadaval olevad tooted:", ", ".join(tooted))

while True:
    toode = input("Sisesta toode (või lõpeta kui oled valmis): ").lower()

    if toode == "lõpeta":
        break

    if toode in tooted:
        kogus = int(input(f"Sisesta, mitu tükki {toode} soovid osta: "))
        ostukorv[toode] = kogus
    else:
        print("Sellist toodet pole saadaval. Proovi uuesti.")

kokku_summa = sum(ostukorv[toode] * hinnad[toode] for toode in ostukorv)

print("\nOSTUTŠEKK:")
for toode, kogus in ostukorv.items():
    hind = hinnad[toode]
    summa = kogus * hind
    print(f"{toode.capitalize()}: {kogus} tk x {hind} € = {summa:.2f} €")

print("\nKokku maksta: {:.2f} €".format(kokku_summa))

#9

a = float(input("Sisesta ruudu külje pikkus a: "))
b = float(input("Sisesta ruudu külje pikkus b: "))

if a == b:
    print("Tegemist on ruuduga.")
else:
    
    print("Ei ole ruut, kuna küljed ei ole võrdsed.")

#10

a = float(input("Sisesta arv a: "))
b = float(input("Sisesta arv b: "))
tehe = input("Sisesta tehe (+, -, *, /): ")
if tehe == '+':
    tulemus = a + b
elif tehe == '-':
    tulemus = a - b
elif tehe == '*':
    tulemus = a * b
elif tehe == '/':
    if b != 0:
        tulemus = a / b
    else:
        tulemus = "Vigane operatsioon (jagamine nulliga)."
else:
    tulemus = "Vigane operatsioon."
print(f"Tulemus: {tulemus}")

#11

sunnipaev = int(input("Sisesta oma sünnipäeva aasta: "))
vanus = 2024 - sunnipaev
juubeli_vahed = [50, 60, 70, 80]
if vanus in juubeli_vahed:
    print("Palju õnne! See on juubeliaasta.")
else:
    print("See ei ole juubeliaasta.")

#12

toote_hind = float(input("Sisesta toote hind eurodes: "))

# Определение процента скидки в зависимости от цены товара
allahindlus_protsent = 10 if toote_hind <= 10 else 20

# Расчет суммы скидки и окончательной стоимости
allahindlus_summa = toote_hind * (allahindlus_protsent / 100)
loplik_hind = toote_hind - allahindlus_summa

# Вывод окончательной стоимости
print(f"Toote hind enne allahindlust: {toote_hind} €")
print(f"Allahindlus {allahindlus_protsent}%: -{allahindlus_summa:.2f} €")
print(f"Lõplik hind: {loplik_hind:.2f} €")

#13

sugu = input("Sisesta oma sugu (mees/naine): ")
if sugu.lower() == "mees":
    
    vanus = int(input("Sisesta oma vanus: "))

    if 18 <= vanus <= 21:
        print("Olete sobiv kandideerima meeskonda.")
    else:
        print("Te ei vasta sobivuse tingimustele.")
elif sugu.lower() == "naine":
    print("Olete sobiv kandideerima meeskonda.")
else:
    print("Sugu ei ole määratud korrektselt.")

# #14

inimeste_arv = int(input("Sisesta inimeste arv: "))
bussi_suurus = int(input("Sisesta bussi suurus: "))

busside_arv = inimeste_arv // bussi_suurus

viimase_bussi_inimesed = inimeste_arv % bussi_suurus

print(f"Vaja on {busside_arv} bussi, et kõik inimesed kohale saaksid.")
print(f"Viimases bussis on {viimase_bussi_inimesed} inimest.")
    