username = input()
distinct = []
for char in username:
    if distinct.__contains__(char):
        continue
    else:
        distinct.append(char)

if len(distinct)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")