number = int(input())
sum = 0
for i in range(number):
    operation = input()
    if operation.__contains__('+'):
        sum += 1
    elif operation.__contains__('-'):
        sum -= 1
print(sum)