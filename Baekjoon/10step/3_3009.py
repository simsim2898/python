a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

if a1 == a2:
    x = a3
elif a1 == a3:
    x = a2
else:
    x = a1
    
if b1 == b2:
    y = b3
elif b1 == b3:
    y = b2
else:
    y = b1

print(x, y)