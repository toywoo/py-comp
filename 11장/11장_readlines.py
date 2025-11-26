infile = open("./11장/phones.txt", "r", encoding="utf-8")
lines = infile.readlines()
print(lines)

for line in lines:
    print(line)

infile.close()