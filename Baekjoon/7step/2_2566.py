box = []
for _ in range(9):
    box.append(list(map(int, input().split())))

maxnum = 0
max_x = 0
max_y = 0

for x in range(9):
    for y in range(9):
        if maxnum <= box[x][y]:
            max_x = x + 1
            max_y = y + 1
            maxnum = box[x][y]
            
print(maxnum)
print(max_x, max_y)