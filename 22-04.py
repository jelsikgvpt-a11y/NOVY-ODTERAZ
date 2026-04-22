from PIL import Image, ImageDraw

image = Image.new("RGB", (400, 400), "white")
draw = ImageDraw.Draw(image)


for i in range(20, 120, 20):
    draw.ellipse((300 - i, 100 - i, 300 + i, 100 + i), outline="black")
draw.ellipse((300, 100, 300, 100), outline="black", width=3)

for i in range(0, 200, 20):
    draw.line((0,200, i+20, 0), fill="blue")

for i in range(0-1, 200, 20):
    draw.line((200,200, 200 -i, 0), fill="red")

for x in range(0,200,20):
    for y in range (200,400,20):
        if (x //20) %2 == (y //20) %2:
            draw.rectangle((x,y,x+20,y+20),outline="black", fill="yellow")
        else:
            draw.rectangle((x,y,x+20,y+20), outline="black", fill="green")


for i in range(0, 200, 20):
    draw.rectangle((200 + i, 200 + i, 220 + i, 220 + i), outline="black", fill="purple")
    
for i in range(0, 200, 20):
    draw.rectangle((380 - i, 200 + i, 400 - i, 220 + i), outline="black", fill="orange")

   
image.show()