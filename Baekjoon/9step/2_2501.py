nk = []
n, k = map(int,input().split())
for i in range(1, n+1):
    if n % i == 0:
        nk.append(i)

if k > len(nk):
    print(0)
else:
    print(nk[k-1])