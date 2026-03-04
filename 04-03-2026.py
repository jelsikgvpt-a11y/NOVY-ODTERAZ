import PIL
from PIL import Image

pic = Image.new(mode="RGB", size=(256, 256), color=("white"))
pixels = pic.load()
for y in range(pic.size[1]):
    for x in range(pic.size[0]):
        #pixels[x, y] = (x, y, 500)
        pixels[x, y] = ((x*y)%256, (x+y)%256,125)
pic.show()
pic.save("mojprvy.jpg")
