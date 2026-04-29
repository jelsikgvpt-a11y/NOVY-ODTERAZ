import math, tkinter as tk, datetime as dt
win = tk.Tk()
win.title("Moje prve hodinky")
s1 = 400
s2 = 400
kratka_ruc = 75
minutova_ruc = 125
sekundova_ruc = 100
hrubka_h = 3
hrubka_m = 2
hrubka_s = 1

canvas = tk.Canvas(win, width=800, height=800, bg="white")
canvas.pack()

def draw():
    cas = dt.datetime.now()
    uhol_hodina = math.radians((cas.hour % 12) * 30 + cas.minute * 0.5 - 90)
    uhol_minuta = math.radians(cas.minute * 6 - 90)
    uhol_sekunda = math.radians(cas.second * 6 - 90)
    print(cas.hour, cas.minute, cas.second)
    canvas.delete("all")
    canvas.create_line(s1, s2, s1 + minutova_ruc * math.cos(uhol_minuta), s2 + minutova_ruc * math.sin(uhol_minuta), fill="black", width=hrubka_m)
    canvas.create_line(s1, s2, s1 + kratka_ruc * math.cos(uhol_hodina), s2 + kratka_ruc * math.sin(uhol_hodina), fill="black", width=hrubka_h)
    canvas.create_line(s1, s2, s1 + sekundova_ruc * math.cos(uhol_sekunda), s2 + sekundova_ruc * math.sin(uhol_sekunda), fill="black", width=hrubka_s)
    canvas.create_oval(s1 - minutova_ruc - 20, s2 - minutova_ruc - 20, s1 + minutova_ruc + 20, s2 + minutova_ruc + 20, outline="black", width=2)
    canvas.after(ms=1000, func=draw)
    for i in range(12):
        uhol = math.radians(i * 30 - 90)
        x = s1 + (minutova_ruc + 10) * math.cos(uhol)
        y = s2 + (minutova_ruc + 10) * math.sin(uhol)
        canvas.create_text(x, y, text=str(i if i != 0 else 12), font=("Arial", 12))
        



draw()
win.mainloop()