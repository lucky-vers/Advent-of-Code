import re

file = open("./input")

twins = []
total_cards = []

for index, line in enumerate(file.readlines()):
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

    twins.append(wins)
    total_cards.append(1)

for index, win in enumerate(twins):
    if win > 0:
        for k in range(total_cards[index]):
            for i in range(index + 1, win + index + 1):
                total_cards[i] += 1

print(sum(total_cards))

file.close()
