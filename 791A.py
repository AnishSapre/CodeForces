limak, bob = map(int, input().split(" "))
years = 0
while 1:
    limak = limak * 3
    bob = bob * 2
    years += 1
    if limak > bob:
        break

print(years)