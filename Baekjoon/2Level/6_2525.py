A,B = map(int, input().split())
C = int(input())
tt = B + C

nh = (A + tt//60)%24
nm = tt%60
print(nh, nm)