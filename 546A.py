k, n, w = map(int, input().split(" "))
total = 0

for i in range(1,w+1):
    total += i * k

if total > n:
    borrow = total - n
    print(borrow)
else: print(0)