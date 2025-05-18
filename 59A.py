word = input()

upper_count, lower_count = 0, 0

for char in word:
    if 97 <= ord(char) <= 122:
        lower_count += 1
    else:
        upper_count += 1
if lower_count > upper_count: print(word.lower())
elif lower_count < upper_count: print(word.upper())
else: print(word.lower())