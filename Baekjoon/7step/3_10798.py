word = []
word2 = []

for _ in range(5):
    a = input()
    word.append(a)
    word2.append(len(a))
    
a = ''
for i in range(max(word2)):
    for j in range(5):
        if i < word2[j]:
            a += word[j][i]
print(a)