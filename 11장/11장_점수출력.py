infile = open('jumsu.txt', 'r', encoding='utf-8')

print('이름, 합계, 평균')

for line in infile:
    line = line.rstrip()
    name, jumsu1, jumsu2, jumsu3 = line.split(",")

    hap = int(jumsu1) + int(jumsu2) + int(jumsu3)
    avg = hap / 3

    print("%s %d %.2f" % (name, hap, avg))

infile.close()
