file = open("./test_input", "r")

contents = file.read().splitlines()

starting_positions = set()

for y, row in enumerate(contents):
    for x, chr in enumerate(row):
        if chr.isdigit() or chr == ".":
            continue

        for i in [y - 1, y, y + 1]:
            for j in [x - 1, x, x + 1]:
                if i < 0 or i >= len(contents) or j < 0 or j >= len(contents) or not contents[i][j].isdigit():
                    continue
                while j > 0 and contents[i][y - 1].isdigit():
                    j -= 1
                starting_positions.add((i, j))

print(starting_positions)

file.close()
