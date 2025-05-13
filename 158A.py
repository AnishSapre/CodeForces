values = input()
n, k = map(int, values.split())

scores = list(map(int, input().split()))
qualified = 0

for i in range(0,n):
    if scores[i] >= scores[k-1] and scores[i] != 0:
        qualified += 1
print(qualified)