numA, numB = input().split()
num1 = int(numA[::-1])
num2 = int(numB[::-1])
if num1 > num2:
    print(num1)
else :
    print(num2)