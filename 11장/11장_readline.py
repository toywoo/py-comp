infile = open("./11장/phones.txt", "r", encoding="utf-8")
lines = infile.readline()

while lines != "":
    print(lines)
    lines = infile.readline()

infile.close()