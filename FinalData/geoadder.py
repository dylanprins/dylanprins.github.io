import csv
with open('editDataBase2009.csv', 'r') as inp, open('postcodetabelgeo.csv', 'r') as geos:
    lst1 = []
    lst2 = []
    for row in csv.reader(inp):
        lst1 += [row]
    for line in csv.reader(geos):
        lst2 += [line]
categories = lst1[0] + ['longitude', 'latitude']
with open('Data2009.txt', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(categories)
    for i in lst1:
        for j in lst2:
            if i[5] == j[0]:
                i[:-2] = [j[3]]
                i[:-1] = [j[4]]
                writer.writerow(i)
with open('Data2009.txt') as inp, open("Data2009.csv", "w") as out:
    lines, mem = inp.readlines(), ''
    for line in lines:
        if line == '\n':
            line = line.replace("\n", "")
        mem += line
    out.write(mem)
    
