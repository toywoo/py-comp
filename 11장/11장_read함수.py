infile = open("./11장/phones.txt", "r", encoding="utf-8")

lines = infile.read()
print(lines)

infile = open("./11장/phones.txt", "r", encoding="utf-8")

lines2 = infile.readline()
print(lines2)

infile.close()