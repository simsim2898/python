word = input().upper()
wordlist = list(set(word))

cnt = [0] * len(wordlist)

for i in range(len(wordlist)):
    cnt[i] = word.count(wordlist[i])

max_count = max(cnt)

if cnt.count(max_count) > 1:
    print("?")
else:
    max_index = cnt.index(max_count)
    print(wordlist[max_index])