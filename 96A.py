team = input()
counter = 0
initial = team[0]
for member in team:
    if member == initial:
        counter += 1
    else:
        initial = member
        counter = 1
    if counter == 7:
        break

if counter == 7:
    print("YES")
else:
    print("NO")