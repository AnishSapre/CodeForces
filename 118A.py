string = input().lower()

vowels = "aoyeui"
result = ""

for char in string:
    if char not in vowels:
        result += "." + char

print(result)
