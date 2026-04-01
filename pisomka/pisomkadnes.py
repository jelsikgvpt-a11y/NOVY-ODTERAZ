import PIL
from PIL import Image
subor = "ciernobiely_obrazok_1 (1).txt"

f = open(subor, "r")
riadky = f.readlines()
f.close()

rozmery = riadky[0].split()
sirka = int(rozmery[0])
vyska = int(rozmery[1])

obrazok = Image.new("L", (sirka, vyska))
pixely = obrazok.load()

y = 0
for riadok in riadky[1:]:
    riadok = riadok.strip ()
    x=0

    i=0
    while i < len(riadok):
        hodnota_nwm = riadok[i:i+2]
        hodnota = int(hodnota_nwm, 16)

        pixely[x,y] = hodnota
        x+=1
        i+=2
    y+=1

obrazok.save("hotovko.png")
print("Hotovo")

