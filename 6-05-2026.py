import tkinter as tk, random
colors = ["green", "red", "gray", "blue", "orange"]
random.shuffle(colors)
sirka = 20
dlzka = 200
wires= []
stop = False



def checker(event):
    objekty = canvas.find_overlapping(event.x, event.y, event.x + 1, event.y + 1)
    if winner in objekty:
        print("Vyhral si!")
        stop = True
        canvas.create_text((20,20), text="Vyhral si!", fill="green", font="Arial 20", anchor="nw")
        stop = True

def timer():
    global cas
    cas = cas - 1
    canvas.itemconfig(hodiny, text=cas)
    if cas>0 and not stop:
        canvas.after(1000, timer)
    else:
        canvas.create_text((20,70),  text="Prehral si!", fill="red", font="Arial 20", anchor="nw")


cas = 60
win = tk.Tk()
canvas = tk.Canvas( win, width=600, height=600, bg="white" )
canvas.pack()
hodiny = canvas.create_text(300,400, text = cas, font=("Arial",45,"bold"), anchor="center")

for i in range(0, len(colors)):
    wires.append(canvas.create_rectangle(200,200+(i*sirka), 200+dlzka, 200+(i+1)*sirka, fill=colors[i], outline="black", width=1))
winner = random.choice(wires)
print(winner)
timer()
canvas.bind("<Button-1>", checker)


win.mainloop()