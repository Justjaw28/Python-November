import math

delitel = 3
je_prvocislo = True

print("Vyber číslo")
print("Rozhodnu, jestli je prvočíslo, nebo ne")
cislo = int(input("Vyber číslo:"))
if cislo < 2:
    je_prvocislo = False
elif cislo == 2:
    je_prvocislo = True
elif cislo % 2 == 0:
    je_prvocislo = False
else:
    while delitel <= math.isqrt(cislo):
        if cislo % delitel == 0:
            je_prvocislo = False
            break
        delitel += 1

if je_prvocislo:
    print(f"{cislo} je prvočíslo: {je_prvocislo}")
else:
    print(f"{cislo} není prvočíslo: {je_prvocislo}")