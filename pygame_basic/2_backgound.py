import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_hight = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_hight))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/jehyu/OneDrive/문서/github/python/pygame_basic/background.png")

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnuing = False
    
    #screen.fill((0,0,255))
    screen.blit(background, (0,0)) # 배경 그리기
    
    pygame.display.update() # 게임화면을 다시 그리기 
# pygame 종료
pygame.quit()