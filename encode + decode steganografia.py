from PIL import Image

sprava = 'Ahoj svet#'  # ten hashtag tam je na to aby vedel kedy ma prestať brať pri decode
obr = Image.open('nature.png')
pixels = obr.load()
dlzka = 8


def priprav(sprava: str) -> list:
    vysledok = []
    for pismenko in sprava:
        cislo = bin(ord(pismenko))[2::]
        pn = dlzka - len(cislo)
        cislo = pn * '0' + cislo
        # print(cislo)
        for j in cislo:
            vysledok.append(int(j))
    # print(vysledok)
    return vysledok


priprav(sprava)


def drticka(sprava):
    spvds = priprav(sprava)
    for i in range(len(spvds)):
        spvds[i]
        sirka = obr.size[0]
        vyska = obr.size[1]
        x = i % (sirka)
        y = i // (sirka)
        pixel_blue = pixels[x, y][2]
        newblue = int(bin(pixel_blue)[2:-1:] + str(spvds[i]), 2)
        newcolour = (pixels[x, y][0], pixels[x, y][1], newblue, pixels[x, y][3])
        # print(pixels[x,y],newcolour, spvds[i])
        pixels[x, y] = newcolour
    obr.save('obrsospr.png')


drticka(sprava)


def decode(obr):
    zoz = []
    last = []
    megastring = ''
    for i in range(obr.size[1]):
        for y in range(obr.size[0]):
            blue = pixels[y, i][2]
            zoz.append(blue)
    for i in zoz:
        if i % 2 == 0:
            last.append(0)
        elif i % 2 == 1:
            last.append(1)
    z = 0
    znak = ""
    while znak != '#':
        smolstr = ''
        for i in range(8):
            smolstr += str(last[z])
            z += 1
        znak = chr(int(smolstr, 2))
        megastring += znak

    print(megastring)


decode(obr)


