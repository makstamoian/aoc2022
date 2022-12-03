f = open("in1.txt", "r")

max1 = 0
max2 = 0
max3 = 0
single_elf = 0

while line := f.readline():
    if line != '\n':
        single_elf += int(line)
    else:
        if single_elf >= max1:
            max3 = max2
            max2 = max1
            max1 = single_elf
        elif single_elf >= max2:
            max3 = max2
            max2 = single_elf
        elif single_elf >= max3:
            max3 = single_elf
        single_elf = 0

print("First part: " + str(max1))
print("Second part: " + str(max1 + max2 + max3))
