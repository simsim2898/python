n = int(input())
num = map(int, input().split())
asd = 0
for a in num:
    error = 0
    if a > 1 :
        for i in range(2, a):  
            if a % i == 0:
                error += 1  
        if error == 0:
            asd += 1  
print(asd)