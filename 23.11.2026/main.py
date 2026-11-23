import time

def ctverec(strana):
    radek = 0
    while radek < strana:       #kreslení řádku
        print("_" * strana)
        radek += 1

def ctverec_duty(strana):
    radek = 0
    while radek < strana:
        if radek == 0 or radek == strana -1:
            print("_" * strana)                         #kreslení 1. a posledního řádku
        else:
            print("_" + " " * (strana - 2) + "_")       #kreslení posledního
        radek += 1

def trojuhel(strana):
    radek = 0
    while radek < strana:
        print("_" * (strana - radek))
        radek += 1
        
def trojuhel_duty(strana):
    radek = 0
    while radek < strana:
        if radek == 0:
            print("_" * strana)
        else:
            print 

opakovat = True
while opakovat:
    trojuhel(5)
    odpoved = input("Chcete další obrazec? [Y/N]")
    if odpoved != "Y":
        opakovat = False

print("Konec programu")