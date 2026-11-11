def vypocet_obsahu(a,b):
    #kontrola stran
    if a < 0 or b < 0:
        return None
    obsah = a * b
    return obsah

# program

print("Výpočet výměry bytu")
print("-------------------")

pocet_mistnposti = int(input("Zadejte počet místností"))
místnost = 1
obsah = 0

while místnost <= pocet_mistnposti:
    print(f"Zadejte rozměry {místnost}. místnosti")
    strana_a = int(input("Zadejte rozměr a"))
    strana_b = int(input("Zadejte rozměr b"))
    obsah += vypocet_obsahu(strana_a, strana_b)
    místnost += 1
print(f"Celková výměra bytu je {obsah}")