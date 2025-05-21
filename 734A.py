number = int(input())
matches = input()
count_A, count_D = 0, 0
for i in matches:
    if i == 'A':
        count_A += 1
    else:
        count_D += 1

if count_A == count_D:
    print("Friendship")
elif count_A < count_D:
    print("Danik")
else:
    print("Anton")