import urllib.request
URL = "https://voskh.cz/envirotyden/index.php?lokalita=lysahora"

odpoved = urllib.request.urlopen(URL)           # odkaz na objeck odpovědi
celkova_srazka = 0
pocet_dnu = 0
radek = odpoved.readline()                      # načtení dat, konec na řádku

while bool (radek):
    text = radek.decode("utf-8").strip()        # vrátí čistý text odpovídající číslu
    srazka = float(text)
    if srazka >=0:
        celkova_srazka += srazka
        pocet_dnu +=1
    radek = odpoved.readline()

odpoved.close()                                  # ukončit komunikaci

print(celkova_srazka / pocet_dnu)