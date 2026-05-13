fr = open("glider-gun.txt", "r")
height = int(fr.readline().strip())
width = int(fr.readline().strip())
dish1 = []
dish2 = []

def create_dishes(height, width):
    global dish1, dish2
    #idem spravit ten prazdny 
    for i in range(height):
        dish2.append([0] * width)
    #dish1 = dish2 #NEFUNGUJE LEBO SU TO SMERNIKY, DOZVIEM SA O TOM NESKOR MOZNO
        dish1.append([0] * width)
    y=0
    x=0
    #prechadzam subor riadok po riadku 
    for riadok in fr:
        x=0
        for znak in riadok.strip():
            if znak != "-":
                dish1[y][x] = 1
            x+=1
        y+=1

def get_neighbour(dish, x, y):
    neighbours = 0
    if x > 0 and dish[y][x-1] == 1: #left
        neighbours += 1
    if x < width - 1 and dish[y][x+1] == 1: #right
        neighbours += 1
    if y > 0 and dish[y-1][x] == 1: #up
        neighbours += 1
    if y < height - 1 and dish[y+1][x] == 1: #down
        neighbours += 1
    if x > 0 and y > 0 and dish[y-1][x-1] == 1: #up-left
        neighbours += 1
    if x < width - 1 and y > 0 and dish[y-1][x+1] == 1: #up-right
        neighbours += 1
    if x > 0 and y < height - 1 and dish[y+1][x-1] == 1: #down-left
        neighbours += 1
    if x < width - 1 and y < height - 1 and dish[y+1][x+1] == 1: #down-right
        neighbours += 1
    return neighbours

create_dishes(height, width)
print(dish1)
print(get_neighbour(dish1, 0, 0))
