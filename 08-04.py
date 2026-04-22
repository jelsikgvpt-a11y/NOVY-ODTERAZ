#sprav obrazok s rozmermi 200x300 a nech sa v nom pixely sachovnicovo striedaju dvoch farbach napriklad biela a cierna co najjednoduchsie


import PIL
from PIL import Image
sirka, vyska = 200, 300
img = Image.new('RGB', (200, 300), color = 'white')
for x in range(sirka):
    for y in range(vyska):
        if(x % 2 == y % 2):
            img.putpixel((x, y), (0, 0, 0))
        
img.show()



        