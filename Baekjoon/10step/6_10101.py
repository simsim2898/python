a = int(input())
b  = int(input())
c  = int(input())

if a == 60 and b == 60 and c == 60:
    print('Equilateral')
elif a+b+c == 180:
    if a == b or a == c or b == c:
        print('Isosceles')
    elif a != b or a != c or b != c:
        print('Scalene')
elif a+b+c != 180:
    print('Error')