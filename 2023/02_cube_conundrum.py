import re

file = open("./input", "r")

games = file.readlines()
index = 1
sum = 0

for i in games:
    result = re.sub(r'^[^:]+: ', '', i).replace('\n', '').replace('; ', ';').replace(', ', ',')
    instances = result.split(';')

    red = []
    blue = []
    green = []

    for ins in instances:
        do = True
        board = [0, 0, 0]
        split_ins = ins.split(',')
        for color in split_ins:
            if 'red' in color:
                red.append(int(re.match("^[0-9]+", color).group()))
            elif 'blue' in color:
               blue.append(int(re.match("^[0-9]+", color).group()))
            elif 'green' in color:
                green.append(int(re.match("^[0-9]+", color).group()))

    sum += (max(red) * max(green) * max(blue))

print(sum)

file.close()
