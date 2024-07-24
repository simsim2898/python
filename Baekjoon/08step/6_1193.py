n = int(input())
a = 1

while n > a:
    n -= a
    a += 1

if a % 2 == 0:
    numerator = n
    denominator = a - n + 1
else:
    numerator = a - n + 1
    denominator = n

print(f"{numerator}/{denominator}")

