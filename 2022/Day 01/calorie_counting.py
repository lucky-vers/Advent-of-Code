file = open("./input", "r")

elves = []

sum = 0

for cal in file.readlines():
    if cal != "\n":
        sum += int(cal)
    else:
        elves.append(sum)
        sum = 0

elves.sort(reverse=True)

print(elves[0] + elves[1] + elves[2])

file.close()
