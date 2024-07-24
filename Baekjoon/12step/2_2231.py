n = int(input())
m = 0
for i in range(1, n+1):
    l = list(map(int, str(i)))
    n = sum(l) + i
    if m == n:
        print(i)
        break
# 아직 덜풀었음​