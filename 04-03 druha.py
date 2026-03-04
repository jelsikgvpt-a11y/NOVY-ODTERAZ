from PIL import Image

pic = Image.open("obrazok1.jpg")
pixels = pic.load()
for y in range(pic.size[1]):
    for x in range(pic.size[0]):
        temp = pixels[x, y] 
        seda = sum(temp) // 3
        pixels[x, y] = (seda, seda, seda)
pic.show()