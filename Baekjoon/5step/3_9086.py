t = int(input())
for _ in range(t):
    word = input()
    print(word[0], word[-1], sep=" ")
    



# 'end=" "'를 사용할경우 출력후 공백을 추가하고 새로운 줄로 이동하지 않음
# 단 print의 경우 기본적으로 출력후 새로운줄로 이동