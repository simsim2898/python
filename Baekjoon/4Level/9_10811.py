n, m = map(int, input().split())

box = [a for a in range(1,n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    binbox = box[i-1:j]
    binbox.reverse()
    box[i-1:j] = binbox

for a in range(n):
    print(box[a], end=" ")