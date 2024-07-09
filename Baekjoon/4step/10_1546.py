n = int(input())
num = list(map(int, input().split())) 

maxnum = max(num)
amean = sum(num) / n
bmean = amean / maxnum * 100
print(bmean)
