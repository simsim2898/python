n, m = map(int, input().split())
ls = list(map(int, input().split()))
a = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum =  ls[i] + ls[j] + ls[k]
            if sum > m:
                continue
            else:
                a.append(sum)
print(max(a))