f = open("input.txt", "r")

res = 0

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

while line := f.readline():
    s1 = line[:len(line) // 2]
    s2 = line[len(line) // 2:]
    found = False
    for x in str(s1):
        for j in str(s2):
            if x == j:
                res += (alphabet.index(x) + 1)
                found = True
            if found:
                break
        if found:
            break

print("First part: " + str(res))

f.seek(0)

res2 = 0

while line := f.readline():
    s1 = line
    s2 = f.readline()
    s3 = f.readline()

    found = False

    for x in s1:
        for j in s2:
            for y in s3:
                if x == j and j == y:
                    res2 += (alphabet.index(x) + 1)
                    found = True
                    break
            if found:
                break
        if found:
            break


print("Second part: " + str(res2))
