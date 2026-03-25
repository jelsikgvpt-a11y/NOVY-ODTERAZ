#šifrovanie a kodovanie je prevod obsahu spravy do inej abecedy pomocou kluca
from PIL import Image
obr = Image.open("Nature_celebrating_India (1).png")
sprava = input("Zadaj mi spravu:")

def sprava_to_bind(message):
    message += "#" #aby som vedel kedy sprava konci
    output = ""
    for char in message:
        
        temp = bin(ord(char))[2::] #premeni cislo na binarny kod ale su na zaciatku 2 znaky "0b" ktore treba odstranit
        if len(temp)<7:
            pocet = 7-len(temp)
            temp = "0"*pocet + temp #doplnim nulu na zaciatok aby bol kod 7 bitov ak je mensi
        output += temp
    return output

def picture_shreder(bm, pic):
    pixels = pic.load() #nacitam pixely z obrazku
    for i in range(len(bm)):
        x = i % pic.size [0]
        y = i // pic.size [0]
        blue_bin = bin(pixels[x,y][2])[2:-1:] #ziskam modry kanal lebo rgb-012, odtrhen 2 prve a posledny znak
        blue_bin = blue_bin + bm[i]
        new_blue = int(blue_bin, 2) 
        pixels[x,y] = (pixels[x,y][0], pixels[x,y][1], new_blue) 
    pic.save("final_pic.png")        


bin_message = sprava_to_bind(sprava)
picture_shreder(bin_message, obr)