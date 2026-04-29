import math, tkinter as tk
win = tk.Tk()
win.title("Drag and drop")
pos_x = -1
pos_y = -1

def click(event):
    global pos_x, pos_y
    print("Klikol si ", event.x, event.y)
    objekty = canvas.find_overlapping(event.x, event.y, event.x+1, event.y+1)
    if objekt_t in objekty:
        pos_x = event.x
        pos_y = event.y

def move_it(event):
    global pos_x, pos_y
    if pos_x != -1:
        vector_x = event.x - pos_x
        vector_y = event.y - pos_y
        pos_x = event.x
        pos_y = event.y
        canvas.move(objekt_t, vector_x, vector_y)


def end_it(event):
    global pos_x, pos_y
    pos_x = -1
    pos_y = -1
    


canvas = tk.Canvas(win, width=800, height=800, bg="white")
canvas.pack()
objekt_t = canvas.create_rectangle(0,0,100,100, fill="hotpink")






canvas.bind("<Button-1>", click)
canvas.bind("<B1-Motion>", move_it)
canvas.bind("<ButtonRelease-1>", end_it)


win.mainloop()