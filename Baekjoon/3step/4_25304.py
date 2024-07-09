tt = int(input())
N = int(input())
X = 0
for _ in range(N):
    a, b = map(int, input().split())
    X += a * b

if X == tt: 
    print("Yes")
else: 
    print("No")
