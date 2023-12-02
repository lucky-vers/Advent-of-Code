file = open("./input", "r")

sums = []

words = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", ]

for line in file.readlines():
    nums = []
    for index, char in enumerate(line):
        if char in '0123456789':
            nums.append(char)

        for i in range(3, 6):
            if line[index:index + i] in words:
                number_in_words = line[index:index + i]
                number = str(words.index(number_in_words) + 1)
                nums.append(number)

    if len(nums) == 1:
        num = 2 * nums[0]
    else:
        num = nums[0] + "" + nums[-1]
    sums.append(int(num))

print(sum(sums))

file.close()
