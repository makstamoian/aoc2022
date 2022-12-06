f = open("input.txt", "r")

datastream = f.readline()


def find_marker(count):
    unique_chars = []
    for i in range(1, len(datastream)):
        if not datastream[i] in unique_chars:
            unique_chars.append(datastream[i])
        else:
            ind = unique_chars.index(datastream[i])
            unique_chars = unique_chars[ind + 1:]
            unique_chars.append(datastream[i])
        if len(unique_chars) == count:
            return i + 1


print(find_marker(4))
print(find_marker(14))
