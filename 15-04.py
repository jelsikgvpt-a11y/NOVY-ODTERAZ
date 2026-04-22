import tkinter as tk
win = tk.Tk()
win.title("moje prve okno")

def akcia():
    global pocitadlo
    print("stlacil si ma", pocitadlo)
    pocitadlo += 1
    farba = canvas.itemcget(obj2, "fill")
    print("farba je", farba)


canvas = tk.Canvas(win, width=800, height=800, bg="cyan")
canvas.pack() #vytvorene objekty dava pod seba 
button = tk.Button(win, text="stlac ma", command=akcia)
button.pack()
obj1 = canvas.create_line(50,50,800,800)
obj2 = canvas.create_rectangle(100,100,500,600, fill="red", outline="blue")
obj3 = canvas.create_oval(400,400,800,700, fill="yellow", outline="green")
print(obj1, obj2, obj3)
canvas.itemconfig(obj2, fill="magenta", width=5)

canvas.itemconfig(obj1, fill="black", width=2)


win.mainloop()
