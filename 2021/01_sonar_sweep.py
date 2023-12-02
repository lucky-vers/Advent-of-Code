file = open("./input", "r")

numbers = file.readlines()
num = 0
three_nums = []

for i in range(len(numbers) - 1):
    if i < len(numbers) - 2:
        prev = int(numbers[i]) + int(numbers[i + 1]) + int(numbers[i + 2])
        three_nums.append(prev)

for i in range(0, len(three_nums) - 1):
    if (three_nums[i + 1] - three_nums[i]) > 0:
        num += 1

print(num)

file.close()
