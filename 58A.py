s = input()
k = 'hello'
j = 0
for char in s:
    if char == k[j]:
        j += 1
        if j == len(k):
            break
if j == len(k):
    print("YES")
else:
    print("NO")
