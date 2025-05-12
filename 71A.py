number = input()

words = []
for i in range(int(number)):
    word = input()
    words.append(word)

for word in words:
    if len(word) > 10:
        result = ''
        result += word[0] + str(len(word) - 2) + word[-1]
        print(result)
    else:
        print(word)