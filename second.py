
def cislo_text(cislo):
    text_cisel = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct",
                "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    text_cisel1 = ["dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    text_cisel2 = ["sto"]
    
    if 0 <= cislo < 20:
        text = (text_cisel[cislo])
        return text
    elif 20 < cislo < 100:
        desitky = cislo // 10
        jednotky = cislo % 10
        text = text_cisel1[desitky - 2]
        if jednotky != 0:
            text += text_cisel[jednotky]
            return text
        else:
            text = text_cisel1[desitky - 2]
            return text
    elif cislo == 100:
        text = (text_cisel2[0])
        return text
    else:
        0 > cislo and cislo < 100
        text = "Číslo musí být v rozsahu od 0 od 100!"
        return text


if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)