n = int(input())
X = []
Y = []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
print((max(X) - min(X)) * (max(Y) - min(Y)))

## a = [] 을 만들때는 for문 앞에 먼저 선언하여야한다.