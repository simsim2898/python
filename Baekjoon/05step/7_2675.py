T = int(input())

for _ in range(T):
    R, word = input().split()
    R = int(R)
    for i in word:
        print(i * R, end='')
    print()