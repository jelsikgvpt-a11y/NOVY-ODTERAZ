from PIL import Image

obr = Image.open("final_pic8.png")

def bin_to_sprava(binarny_text):
    output = ""
    for i in range(0, len(binarny_text), 7):
        znak_bin = binarny_text[i:i+7]
        if len(znak_bin) < 7:
            break
        znak = chr(int(znak_bin, 2))
        if znak == "#":  # koniec správy
            break
        output += znak
    return output

def picture_reader(pic):
    pixels = pic.load()
    bin_message = ""

    for i in range(pic.size[0] * pic.size[1]):
        x = i % pic.size[0]
        y = i // pic.size[0]

        blue = pixels[x, y][2]
        blue_bin = bin(blue)[2:]  # premena na binárne

        bin_message += blue_bin[-1]  # vezmem posledný bit

    sprava = bin_to_sprava(bin_message)
    return sprava

decoded_message = picture_reader(obr)
print("Skrytá správa je:", decoded_message)