word1 = input()
word2 = input()

word2_reversed = word2[::-1]

if word1 == word2_reversed:
    print("YES")
else:
    print("NO")