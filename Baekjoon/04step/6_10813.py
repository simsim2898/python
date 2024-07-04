n, m = map(int, input().split())
box = [i for i in range(1, n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    box[i-1], box[j-1] = box[j-1], box[i-1] 
for box in box:
    print(box, end=' ') 
