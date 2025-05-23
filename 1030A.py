people = int(input())
opinions = list(map(int, input().split(" ")))

if opinions.__contains__(1):
    print("HARD")
else:
    print("EASY")