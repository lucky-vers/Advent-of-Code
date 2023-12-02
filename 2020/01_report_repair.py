file = open("./input", "r")

nums = file.readlines()
num = 0

for num1 in nums:
    for num2 in nums:
        if str(2020 - int(num1) - int(num2)) + "\n" in nums:
            num = int(num1) * int(num2) * (2020 - int(num1) - int(num2))
            break

print(num)
