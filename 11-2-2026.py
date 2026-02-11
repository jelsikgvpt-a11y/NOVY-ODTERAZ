# uloha 4 maturita: záznamy z meteorologických staníc
fr = open("subory2/meteostanice.txt", "r", encoding="utf-8")
fw = open("subory2/moje_vystupy", "w", encoding="utf-8")
counter = 0
max_teplota = -1000
temperatures = []
for row in fr:
    processed_line = row.strip().split(" ")
    temperatures.append(float(processed_line[3].replace(",", ".")))
    print(processed_line)
    counter += 1
print(f"Počet meraní: {counter}")
fw.write(f"Počet meraní: {counter}\n")
print(f"Teploty su: {temperatures}")
print(f"Priemerná teplota: {sum(temperatures) / len(temperatures)}")
print(f"Najvysia teplota: {max(temperatures)}")
fw.write(f"Priemerná teplota: {sum(temperatures) / len(temperatures)}\n")
fw.write(f"Najvysia teplota: {max(temperatures)}\n")

fw.close()
