import random

tajne_cislo = random.randint(1, 20)
pokusy = 0
tip = 0
max_pokusy = 5

while tip != tajne_cislo and pokusy < max_pokusy:
    tip = int(input("Hádej číslo: "))
    if tip < 1 or tip > 20:
        print("Číslo musí být mezi 1 a 20.")
        continue
    pokusy += 1
    if tip < tajne_cislo:
        print("Hledej vyšší číslo.")
    elif tip > tajne_cislo:
        print("Hledej nižší číslo.")

if tip == tajne_cislo:
    print(f"Gratulace! Uhádl jsi číslo {tajne_cislo} po {pokusy} pokusech.")
else:
    print(f"Prohrál jsi. Tajné číslo bylo {tajne_cislo}.")