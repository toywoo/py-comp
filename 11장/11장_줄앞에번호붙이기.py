infile = open("proverbs.txt", "r")
outfile = open("output.txt", "w")

i = 1

for line in infile:
    outfile.write(str(i) + ": " + line)
    i = i + 1

infile.close()
outfile.close()

infile	=	open('output.txt',	'r')
line=infile.read()
print(line)
infile.close()