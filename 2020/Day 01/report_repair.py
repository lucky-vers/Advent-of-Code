file = open("./input", "r")

nums = file.readlines()

for num in nums:
    if str(2020 - int(num)) + "\n" in nums:
        print(2020 * int(num) - int(num) ** 2)
        break

