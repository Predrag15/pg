def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    if cislo == 2:
        return True
    if cislo % 2 == 0:
        return False
    for i in range(3, int(cislo ** 0.5) + 1, 2):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(cislo):
    return [cislo for cislo in range(2, cislo + 1) if je_prvocislo(cislo)]

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)