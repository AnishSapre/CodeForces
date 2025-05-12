number = input()
problems = 0

for i in range(int(number)):
    petya, vasya, tonya = input().split(" ")
    if int(petya) + int(vasya) + int(tonya) >= 2:
        problems += 1

print(problems)