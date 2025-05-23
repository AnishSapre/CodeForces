year = int(input())
year += 1
while 1:
    temp = str(year)
    res = ''.join(set(temp))
    if len(res) == len(temp):
        print(temp)
        break
    else:
        year += 1

