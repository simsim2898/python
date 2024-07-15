# 1차원 배열의 경우 EX): a = [0 for i in range(n)], 2차원 배열의 경우 a = [[0 for i in range(n] for j in range(n)]
white = [[0 for _ in range(100)] for _ in range(100)]
result  = 0
n = int(input())
for _ in range(n):
    x, y = list(map(int, input().split()))
    
    for white_x in range(x, x+10):
        for white_y in range(y, y+10):
            white[white_x][white_y] = 1   # 칸당 계산   
            
    result = sum(sum(a) for a in white) # 만들어둔 행열 1 계산 합 for 문으로 문제 풀기 가능
print(result)