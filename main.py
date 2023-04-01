han_tu = open("D:\\.Repo\\Tieng_Nhat\\han_tu.txt", mode = "r", encoding="utf8")

datas = han_tu.read().split("\n")

kanji = []
nghia = []

for data in datas:
    data = data.split("\t")
    kanji.append(data[0])
    if data[1] == "":
        data[1] = "NULL"
    nghia.append(data[1])

# Main
inp = open("D:\\.Repo\\Tieng_Nhat\\inp.txt", mode = "r", encoding="utf8")
datas = inp.read().split("\n")

outp = open("D:\\.Repo\\Tieng_Nhat\\outp.txt", mode = "w", encoding="utf8")
for data in datas:
    data = [*data]
    for i in data:
        try:
            index = kanji.index(i)
            outp.write(nghia[index] + " ")
        except:
            continue
    outp.write("\n")

