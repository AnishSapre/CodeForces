distance = int(input())
count = 0

while distance > 0:
    if distance == 1 or distance == 2 or distance == 3 or distance == 4:
        count += 1
        break
    else:
        distance -= 5
    count += 1
print(count)