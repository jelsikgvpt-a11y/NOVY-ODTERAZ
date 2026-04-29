import math, tkinter as tk, datetime as dt
win = tk.Tk()
win.title("Moje prve hodinky")
s1 = 400
s2 = 400
kratka_ruc = 75
dlha_ruc = 150
hrubka_h = 3
hrubka_m = 1



cas = dt.datetime.now()
print(cas.hour, cas.minute, cas.second)
uhol_minuta = math.radians(cas.minute * 6 - 90)
uhol_hodina = math.radians(cas.hour * 30 + cas.minute * 0.5 - 90)



canvas = tk.Canvas(win, width=800, height=800, bg="white")
canvas.pack()
canvas.create_line(s1,s2, s1 + dlha_ruc * math.cos(uhol_minuta), s2 + dlha_ruc * math.sin(uhol_minuta), fill="black", width=hrubka_m)

canvas.create_line(s1,s2, s1 + kratka_ruc * math.cos(math.radians(cas.second * 6 - 90)), s2 + kratka_ruc * math.sin(math.radians(cas.second * 6 - 90)), fill="black", width=hrubka_h)
canvas.create_text



win.mainloop()
