import random
import time

max = 20
min = 1
horni = max
spodni = min

cislo = int(input(f"Zadej vaše tajné číslo mezi 1 a {max}: "))
if cislo < 1 or cislo > max:
    print("Číslo musí být mezi 1 a max. Nastavuji náhodné.")
    cislo = random.randint(1, max)
    print (f"Vaše tajné číslo je: {cislo}, ale to já nevím ;]")

vybrani = (horni + spodni) // 2
pokusy = 0

while vybrani != cislo:
    print(f"Vybral jsem {vybrani}")
    if vybrani < cislo:
        print("Hledám vyšší číslo.")
        spodni = vybrani + 1
        pokusy += 1
        time.sleep(1)
    elif vybrani > cislo:
        print("Hledám nižší číslo.")
        horni = vybrani - 1
        pokusy += 1
        time.sleep(1)
    vybrani = (horni + spodni) // 2
        

print(f"Uhádl jsem číslo {cislo} na {pokusy} pokusů.")