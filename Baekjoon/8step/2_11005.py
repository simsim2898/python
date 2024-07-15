n, b = map(int, input().split())
number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ten = ''
while n != 0:
    ten = ten + str(number[n % b])
    n //= b
print(ten[::-1])