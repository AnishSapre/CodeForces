matrix = []

for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            x = i
            y = j

moves = 0
moves += abs(x-2)
moves += abs(y-2)

print(moves)