f = open("input.txt", "r")

res_part1 = 0

while line := f.readline():
    my_turn = ""
    elf_turn = ""
    if line[2] == "X":
        my_turn = "A"
        res_part1 += 1
    elif line[2] == "Y":
        my_turn = "B"
        res_part1 += 2
    elif line[2] == "Z":
        my_turn = "C"
        res_part1 += 3

    elf_turn = line[0]

    if my_turn == elf_turn:
        res_part1 += 3
    elif elf_turn == "A":
        if my_turn == "B":
            res_part1 += 6
        if my_turn == "C":
            res_part1 += 0
    elif elf_turn == "B":
        if my_turn == "C":
            res_part1 += 6
        if my_turn == "A":
            res_part1 += 0
    elif elf_turn == "C":
        if my_turn == "A":
            res_part1 += 6
        if my_turn == "B":
            res_part1 += 0

print("First part: " + str(res_part1))

f.seek(0)
res_part2 = 0

while line := f.readline():
    if line[2] == "Y":
        res_part2 += 3
        if line[0] == "A":
            res_part2 += 1
        elif line[0] == "B":
            res_part2 += 2
        elif line[0] == "C":
            res_part2 += 3

    elif line[2] == "X":
        res_part2 += 0
        if line[0] == "A":
            res_part2 += 3
        elif line[0] == "B":
            res_part2 += 1
        elif line[0] == "C":
            res_part2 += 2

    elif line[2] == "Z":
        res_part2 += 6
        if line[0] == "A":
            res_part2 += 2
        elif line[0] == "B":
            res_part2 += 3
        elif line[0] == "C":
            res_part2 += 1

print("Second part: " + str(res_part2))
