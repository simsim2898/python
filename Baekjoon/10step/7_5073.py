while True:
    x, y, z = map(int, input().split())
    m = max(x, y, z)
    if x == 0 and y == 0 and z == 0:
        break
    elif m >= x + y + z - m:
        print('Invalid')
    elif x == y == z:
        print('Equilateral')
    elif x == y or x == z or y == z:
        print('Isosceles')
    else:
        print('Scalene')