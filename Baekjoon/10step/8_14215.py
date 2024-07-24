a, b, c = map(int, input().split())
ma = max(a, b, c)
mi = min(a, b, c)
sum = a + b + c
middle = sum - ma - mi  # 중간값

if ma >= middle + mi:
    print(2 * (middle + mi) - 1)
else:
    print(sum)