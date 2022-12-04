f = open("input.txt", "r")

res1 = 0

while line := f.readline():
    str1, str2 = line.split(',')
    beg1, end1 = str1.split('-')
    beg2, end2 = str2.split('-')
    if (int(beg1) <= int(beg2) and int(end1) >= int(end2)) or (int(beg2) <= int(beg1) and int(end2) >= int(end1)):
        res1 += 1

print("First part: ", str(res1))

f.seek(0)


res2 = 0

while line := f.readline():
    str1, str2 = line.split(',')
    beg1, end1 = str1.split('-')
    beg2, end2 = str2.split('-')
    if (int(beg2) <= int(beg1) <= int(end2)) or \
       (int(beg1) <= int(end2) <= int(end1)) or \
       (int(beg1) <= int(beg2) <= int(end1)) or \
       (int(beg2) <= int(end1) <= int(end2)):
        res2 += 1

print("Second part: ", str(res2))
