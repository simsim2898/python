import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_hight = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_hight))

pygame.display.set_caption("Nado Game")

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnuing = False

# pygame 종료
pygame.quit()