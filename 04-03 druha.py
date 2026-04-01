from PIL import Image

pic = Image.open("obrazok1.jpg")
pic2 = Image.new(mode = "RGB", size=(pic.size[0], pic.size[1]), color = ("white"))
pixels = pic.load()
pixels2 = pic2.load()
for y in range(pic.size[1]):
    for x in range(pic.size[0]):
        #otočit o 180 stupňů obrázok kod s + a -        from PIL import Image
        
        w, h = 256, 256
        orig = Image.new("RGB", (w, h), "white")
        op = orig.load()
        for y in range(h):
            for x in range(w):
                op[x, y] = ((x*y) % 256, (x+y) % 256, 125)
        
        rot = Image.new("RGB", (h, w))            # rozmery sa vymenia
        rp = rot.load()
        for y in range(h):                        # pre každý pixel pôvodného
            for x in range(w):
                new_x = h - 1 - y                 # mapovanie súradníc
                new_y = x
                rp[new_x, new_y] = op[x, y]
        
        rot.show()
        rot.save("mojprvy_rotated.jpg")

        

pic2.show()