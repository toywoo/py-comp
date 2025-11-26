infile = open("./11장/proverbs.txt", "r", encoding="utf-8")

for line in infile:
    print(line.rstrip())


infile.close()