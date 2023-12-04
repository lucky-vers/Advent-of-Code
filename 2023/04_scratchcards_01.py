import re

file = open("./input")

sum = 0

for line in file.readlines():
    line = line.replace('\n', '')
    line = re.sub("Card\s+[0-9]+:\s+", "", line)
    line = re.sub("\s+", " ", line)
    line = re.sub(" \| ", "|", line)
    line = line.split('|')

    winnums = line[0].split(' ')
    mynums  = line[1].split(' ')

    wins = 0

    for num in mynums:
        if num in winnums:
            wins += 1

    if wins >= 1:
        sum += (2 ** ( wins - 1 ))

print(sum)

file.close()
