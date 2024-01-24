# print("Tere maailm")
# nimi=input("Mis on sinu nimi?")
# vanus=int(input("Kui vana sa oled?"))

# print("Tere "+nimi+"! Sa oled "+str(vanus)+" aastat vana.")
# print("Tere",nimi,"! Sa oled",vanus,"aastat vana.")
# print("Tere {0}! Sa oled {1} aastat vana".format(nimi,vanus))

# print(type(nimi))
# print(type(vanus))

#arv1=float(input("Arv 1: "))
#t=input("Tehe: ")
#arv2=float(input("Arv 2: "))
#vastus=eval(str(arv1)+t+str(arv2))
#print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus))

#vanus = 18
#eesnimi = "Jaak"
#pikkus = 16.5
#kas_käib_koolis = True
#print("Muutuja",vanus,"on",type(vanus))
#print("Muutuja",eesnimi,"on",type(eesnimi))
#print("Muutuja",pikkus,"on",type(pikkus))
#print("Muutuja",kas_käib_koolis,"on",type(kas_käib_koolis))

#from random import * #kõik funktsioonid mis on moodulis
#kogus=randint(1,100) #66
#print("Kokku on",kogus,"kommid")
#mitu=int(input("Mitu kommi tahad võtta")) #33
#kogus=kogus-mitu #kogus=kogus-mitu->kogus-=mitu
#print("Laua peal on",kogus,"kommid")

#from math import *
#l=float(input("Ümbermõõt:"))
#d=round(l/pi,2)  
#print("Läbimõõt=", d)
#1.5

# def jagub_kolmega(arv):
#     if arv % 3 == 0:
#         return True
#     else:
#         return False

# def main():
#     # Küsi kasutajalt täisarv
#     arv = int(input("Sisesta täisarv: "))

#     # Kontrolli, kas arv jaguneb kolmega ilma jäägita
#     if jagub_kolmega(arv):
#         print("Sisestatud arv jagub kolmega ilma jäägita.")
#     else:
#         print("Sisestatud arv ei jagu kolmega ilma jäägita.")

# if __name__ == "__main__":
#     main()
    
#     def jagub_kolmega(arv):
#     if arv % 3 == 0:
#         return True
#     else:
#         return False

# def main():
#     # Küsi kasutajalt täisarv
#     arv = int(input("Sisesta täisarv: "))

#     # Kontrolli, kas arv jaguneb kolmega ilma jäägita
#     if jagub_kolmega(arv):
#         print("Sisestatud arv jagub kolmega ilma jäägita.")
#     else:
#         print("Sisestatud arv ei jagu kolmega ilma jäägita.")

# if __name__ == "__main__":
#     main()
    
# def eksamivorm(oppilaste_arv):
#     eksamivormid = []
#     for i in range(oppilaste_arv):
#         eksamivormid.append({"Õpilane": f"Õpilane {i + 1}", "Eksam1": "", "Eksam2": "", "Eksam3": ""})
#     return eksamivormid

# def main():
#     # Küsi õpilaste arvu
#     oppilaste_arv = int(input("Sisesta õpilaste arv: "))

#     # Looge eksamivormid ja kuva tulemused
#     eksamivormid = eksamivorm(oppilaste_arv)
#     for vorm in eksamivormid:
#         print(vorm)
        
# def vordle_kotte(kaal1, kaal2):
#     if kaal1 > kaal2:
#         return "Esimene kott on raskem."
#     elif kaal1 < kaal2:
#         return "Teine kott on raskem."
#     else:
#         return "Mõlemad kotid kaaluvad sama palju."

# def main():
#     # Küsi kaalud
#     kaal1 = float(input("Sisesta esimese koti kaal (kg): "))
#     kaal2 = float(input("Sisesta teise koti kaal (kg): "))

#     # Võrdle kaale ja kuva tulemus
#     tulemus = vordle_kotte(kaal1, kaal2)
#     print(tulemus)

# if __name__ == "__main__":
#     main()
    
#1.6
# def suurem_arv(arv1, arv2):
#     if arv1 > arv2:
#         return arv1
#     else:
#         return arv2

# def main():
#     # Küsi kaks sisendarvu
#     arv1 = float(input("Sisesta esimene arv: "))
#     arv2 = float(input("Sisesta teine arv: "))

#     # Leia suurem arv ja kuva tulemus
#     suurem = suurem_arv(arv1, arv2)
#     print(f"Suurem arv on: {suurem}")

# if __name__ == "__main__":
#     main()
    

#3
def main():
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
if __name__ == "__main__":
    main()

#4
def calculate_discounted_price(original_price):
    discount_rate = 0.3  # 30% скидка
    if original_price > 700:
        discounted_price = original_price * (1 - discount_rate)
        return discounted_price
    else:
        return original_price

def main():
    original_price = float(input("Введите первоначальную цену компьютера в евро: "))
    discounted_price = calculate_discounted_price(original_price)

    print(f"Цена со скидкой: {discounted_price} евро.")

if __name__ == "__main__":
    main()

#5
def main():
    # Küsi temperatuur kasutajalt
    temperatuur = float(input("Sisesta temperatuur kraadides: "))

    # Kontrolli, kas temperatuur on üle 18 kraadi
    if temperatuur > 18:
        print("Temperatuur on üle 18 kraadi, soovitav toasoojus talvel.")
    else:
        print("Temperatuur on 18 kraadi või alla selle, võib olla jahe talvel.")

if __name__ == "__main__":
    main()

#6
def main():
    # Küsi inimese pikkust kasutajalt
    pikkus = float(input("Sisesta inimese pikkus meetrites: "))

    # Määra piirid lühikese, keskmise ja pika jaoks
    luhike_pikkus = 1.60
    pikk_pikkus = 1.80

    # Kontrolli, millisesse kategooriasse pikkus kuulub
    if pikkus < luhike_pikkus:
        print("Inimene on lühike.")
    elif luhike_pikkus <= pikkus <= pikk_pikkus:
        print("Inimene on keskmise pikkusega.")
    else:
        print("Inimene on pikk.")

if __name__ == "__main__":
    main()

#7
def main():
    # Küsi inimese pikkust kasutajalt
    pikkus = float(input("Sisesta inimese pikkus meetrites: "))

    # Küsi inimese sugu kasutajalt
    sugu = input("Sisesta inimese sugu (mees/naine): ").lower()

    # Määra piirid lühikese, keskmise ja pika jaoks
    luhike_pikkus = 1.60
    keskmine_pikkus_mees = 1.75
    pikk_pikkus_mees = 1.90
    keskmine_pikkus_naine = 1.65
    pikk_pikkus_naine = 1.80

    # Kontrolli, millisesse kategooriasse pikkus ja sugu kuuluvad
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

if __name__ == "__main__":
    main()

#8
import random

def main():
    tooted = ["piim", "saia", "leiba", "juust", "vorst"]
    hinnad = {toode: round(random.uniform(1, 5), 2) for toode in tooted}  # Juhuslikud hinnad

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

    # Arvuta ostusumma ja kuva tšekk
    kokku_summa = sum(ostukorv[toode] * hinnad[toode] for toode in ostukorv)
    
    print("\nOSTUTŠEKK:")
    for toode, kogus in ostukorv.items():
        hind = hinnad[toode]
        summa = kogus * hind
        print(f"{toode.capitalize()}: {kogus} tk x {hind} € = {summa:.2f} €")

    print("\nKokku maksta: {:.2f} €".format(kokku_summa))

if __name__ == "__main__":
    main()

#9
1. Sisesta ruudu küljed a ja b.
2. Kui a on võrdne b-ga, siis ruut on võimalik.
3. Vastasel juhul, ruut ei ole võimalik.
4. Väljasta vastav teade.
def kas_on_ruut(a, b):
    if a == b:
        return True
    else:
        return False

def main():
    # Sisesta ruudu küljed
    a = float(input("Sisesta ruudu külje pikkus a: "))
    b = float(input("Sisesta ruudu külje pikkus b: "))

    # Kontrolli, kas tegemist on ruuduga
    if kas_on_ruut(a, b):
        print("Tegemist on ruuduga.")
    else:
        print("Ei ole ruut, kuna küljed ei ole võrdsed.")

if __name__ == "__main__":
    main()

#10
1. Sisesta arv a.
2. Sisesta arv b.
3. Sisesta tehe (+, -, *, /).
4. Kui tehe on '+', siis väljasta a + b.
5. Kui tehe on '-', siis väljasta a - b.
6. Kui tehe on '*', siis väljasta a * b.
7. Kui tehe on '/', siis väljasta a / b.
8. Vastasel juhul väljasta "Vigane operatsioon".
def kalkulaator(a, b, tehe):
    if tehe == '+':
        return a + b
    elif tehe == '-':
        return a - b
    elif tehe == '*':
        return a * b
    elif tehe == '/':
        if b != 0:
            return a / b
        else:
            return "Vigane operatsioon (jagamine nulliga)."
    else:
        return "Vigane operatsioon."

def main():
    # Sisesta arvud ja tehe
    a = float(input("Sisesta arv a: "))
    b = float(input("Sisesta arv b: "))
    tehe = input("Sisesta tehe (+, -, *, /): ")

    # Kalkuleeri ja väljasta vastus
    tulemus = kalkulaator(a, b, tehe)
    print(f"Tulemus: {tulemus}")

if __name__ == "__main__":
    main()

#11
 def kas_on_juubel(sunnipaev):
    vanus = 2024 - sunnipaev  # Eeldades, et praegu on aasta 2024
    juubeli_vahed = [60, 70, 80, 90]  # Juubeli vanused

    if vanus in juubeli_vahed:
        return True
    else:
        return False

def main():
    # Küsi kasutajalt sünnipäeva
    sunnipaev = int(input("Sisesta oma sünnipäeva aasta: "))

    # Kontrolli, kas tegemist on juubeliga
    if kas_on_juubel(sunnipaev):
        print("Palju õnne! See on juubeliaasta.")
    else:
        print("See ei ole juubeliaasta.")

if __name__ == "__main__":
    main()

#12
def main():
    # Küsi kasutajalt toote hind
    toote_hind = float(input("Sisesta toote hind eurodes: "))

    # Määra allahindluse määr vastavalt tingimustele
    if toote_hind <= 10:
        allahindlus_protsent = 10
    else:
        allahindlus_protsent = 20

    # Arvuta allahindlus ja lõplik hind
    allahindlus_summa = toote_hind * (allahindlus_protsent / 100)
    loplik_hind = toote_hind - allahindlus_summa

    # Kuva lõplik hind
    print(f"Toote hind enne allahindlust: {toote_hind} €")
    print(f"Allahindlus {allahindlus_protsent}%: -{allahindlus_summa:.2f} €")
    print(f"Lõplik hind: {loplik_hind:.2f} €")

if __name__ == "__main__":
    main()

#13
def kontrolli_sobivust(sugu, vanus):
    if sugu.lower() == "mees":
        if 16 <= vanus <= 18:
            return True
        else:
            return False
    elif sugu.lower() == "naine":
        return True  # Kui kandideerija on naissoost, ei küsita vanust
    else:
        return False  # Kui sugu ei ole "mees" ega "naine"

def main(): #komment
    # Küsi kandideerija sugu
    sugu = input("Sisesta oma sugu (mees/naine): ")

    # Kontrolli, kas küsida vanust või mitte
    if sugu.lower() == "mees":
        # Küsi kandideerija vanust
        vanus = int(input("Sisesta oma vanus: "))

        # Kontrolli sobivust vastavalt vanusele
        if kontrolli_sobivust(sugu, vanus):
            print("Olete sobiv kandideerima meeskonda.")
        else:
            print("Te ei vasta sobivuse tingimustele.")
    elif sugu.lower() == "naine":
        print("Olete sobiv kandideerima meeskonda.")
    else:
        print("Sugu ei ole määratud korrektselt.")

if __name__ == "__main__":
    main()

#14
def kontrolli_sobivust(sugu, vanus):
    if sugu.lower() == "mees":
        if 16 <= vanus <= 18:
            return True
        else:
            return False
    elif sugu.lower() == "naine":
        return True  # Kui kandideerija on naissoost, ei küsita vanust
    else:
        return False  # Kui sugu ei ole "mees" ega "naine"

def main():
    # Küsi kandideerija sugu
    sugu = input("Sisesta oma sugu (mees/naine): ")

    # Kontrolli, kas küsida vanust või mitte
    if sugu.lower() == "mees":
        # Küsi kandideerija vanust
        vanus = int(input("Sisesta oma vanus: "))

        # Kontrolli sobivust vastavalt vanusele
        if kontrolli_sobivust(sugu, vanus):
            print("Olete sobiv kandideerima meeskonda.")
        else:
            print("Te ei vasta sobivuse tingimustele.")
    elif sugu.lower() == "naine":
        print("Olete sobiv kandideerima meeskonda.")
    else:
        print("Sugu ei ole määratud korrektselt.")

if __name__ == "__main__":
    main()


    