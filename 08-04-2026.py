#musime urobit ciaru z bodov A a B pomocou niakeho vzorcu
import PIL
from PIL import Image



sirka, vyska = 200, 300
img = Image.new('RGB', (200, 300), color = 'white')
a1=2
a2=2

b1=10
b2=5

A = (a1, a2)    
B = (b1, b2)    
a = ((a2-b2)/(a1-b1))            
b = a2-a*((a2-b2)/(a1-b1))
if abs(a1-b1)>abs(a2-b2):
   for x in range(a1, b1+1):
         y = int(a*x+b)
         img.putpixel((x, y), (0, 0, 0))
else:   
     for y in range(a2, b2+1):
         x = int((y-b)/a)
         img.putpixel((x, y), (0, 0, 0))    
    

img.show()