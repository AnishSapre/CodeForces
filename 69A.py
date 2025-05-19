matrix = []
n = int(input())  # Read the number of vectors
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

x, y, z = 0, 0, 0

for i in range(n):
    x += matrix[i][0]
    y += matrix[i][1]
    z += matrix[i][2]

if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")