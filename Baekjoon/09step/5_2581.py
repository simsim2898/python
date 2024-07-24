m = int(input())
n = int(input())

sosu= []

for a in range(m, n+1): 
    b = 0 
    if a > 1: 
        for c in range(2, a): 
            if a % c == 0: 
                b = b + 1 
                break
        
        if b == 0:
            sosu.append(a)
            
if len(sosu) > 0:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)