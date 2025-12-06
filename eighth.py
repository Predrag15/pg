def bin_to_dec(binarni_cislo):
    binarni_cislo = str(binarni_cislo)

    for znak in binarni_cislo:
        if znak not in "01":
            raise ValueError("Neplatné binární číslo")

    dec = 0
    for bit in binarni_cislo:
        dec = dec * 2 + int(bit)

    return dec


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128