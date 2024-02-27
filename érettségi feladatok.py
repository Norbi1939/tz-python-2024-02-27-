# 1-ső feladat
ösvények = []
f = open("osvenyek.txt", "r", encoding="UTF-8")
for sor in f:
    ösvények.append(sor.replace("\n",""))
f.close()

dobások = []
segéd = []
f = open("dobasok.txt", "r", encoding="UTF-8")
for sor in f:
    segéd.append(sor.replace("\n","").strip().split())
i = 0
while i < len(segéd[0]):
    dobások.append(int(segéd[0][i]))
    i += 1

# 2.feladat
print(f"a dobások száma: {len(dobások)}")
print(f"Az ösvények száma: {len(ösvények)}")

# 3.feladat  
maxÉrték = len(ösvények[0])
maxHely = 0
i= 1
while i < len(ösvények):
    if len(ösvények[i]) > maxÉrték:
        maxÉrték = len(ösvények[i])
        maxHely = i
    i += 1
print(F"\nAz egyik leghosszabb a(z) {maxHely +1}. ösvény, hossza: {maxÉrték} ")

# 4.feladat
ösvénySorszám = int(input("Adja meg egy ösvény sorszámát!"))
JátékosokSzáma = int(input("Adja meg a játékosok számát!"))

# 5.feladat (HF)
# indexek: 0: M, 1: E, 2: V
hisztogram = [0,0,0]
i = 0
while i < len(ösvények[ösvénySorszám - 1]):
    if ösvények[ösvénySorszám - 1][i] == "M":
        hisztogram[0] += 1
    elif ösvények[ösvénySorszám - 1][i] == "E":
        hisztogram[1] += 1
    elif ösvények[ösvénySorszám - 1][i] == "V":
        hisztogram[2] += 1
    i += 1
print(f"M: {hisztogram[0]}. darab")
print(f"E: {hisztogram[1]}. darab")
print(f"V: {hisztogram[2]}. darab")

