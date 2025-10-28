def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka["typ"]
    radek, sloupec = figurka["pozice"]
    cil_r, cil_s = cilova_pozice

    if not (1 <= cil_r <= 8 and 1 <= cil_s <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    def je_volna_cesta(od, do, obsazene):
        r1, s1 = od
        r2, s2 = do
        dr = (r2 - r1)
        ds = (s2 - s1)
        krok_r = (dr // abs(dr)) if dr != 0 else 0
        krok_s = (ds // abs(ds)) if ds != 0 else 0
        r, s = r1 + krok_r, s1 + krok_s

        while (r, s) != (r2, s2):
            if (r, s) in obsazene:
                return False
            r += krok_r
            s += krok_s
        return True

    if typ == "pěšec":
        if cil_s != sloupec:
            return False
        if cil_r == radek + 1 and (cil_r, cil_s) not in obsazene_pozice:
            return True
        if radek == 1 and cil_r == 3:  
            if (2, sloupec) not in obsazene_pozice and (3, sloupec) not in obsazene_pozice:
                return True
        return False

    elif typ == "jezdec":
        return (abs(cil_r - radek), abs(cil_s - sloupec)) in [(2, 1), (1, 2)]

    elif typ == "věž":
        if radek == cil_r or sloupec == cil_s:
            return je_volna_cesta((radek, sloupec), (cil_r, cil_s), obsazene_pozice)
        return False

    elif typ == "střelec":
        if abs(cil_r - radek) == abs(cil_s - sloupec):
            return je_volna_cesta((radek, sloupec), (cil_r, cil_s), obsazene_pozice)
        return False

    elif typ == "dáma":
        if (radek == cil_r or sloupec == cil_s) or (abs(cil_r - radek) == abs(cil_s - sloupec)):
            return je_volna_cesta((radek, sloupec), (cil_r, cil_s), obsazene_pozice)
        return False

    elif typ == "král":
        return max(abs(cil_r - radek), abs(cil_s - sloupec)) == 1

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
