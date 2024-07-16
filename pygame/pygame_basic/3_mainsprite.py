import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/jehyu/OneDrive/문서/github/python/pygame_basic/background.png")

# 캐리터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/jehyu/OneDrive/문서/github/python/pygame_basic/character.png") 
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0]
character_hight = character_size[0]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_hight
#이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnuing = False
    
    screen.blit(background, (0,0)) # 배경 그리기
    
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # 게임화면을 다시 그리기 
# pygame 종료
pygame.quit()