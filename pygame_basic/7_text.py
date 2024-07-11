import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/jehyu/OneDrive/문서/github/python/pygame_basic/background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:/Users/jehyu/OneDrive/문서/github/python/pygame_basic/character.png") 
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0]
character_height = character_size[0]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 기본 좌표 설정
to_x = 0
to_y = 0

# 속도
character_speed = 0.6

# 몹
mob = pygame.image.load("C:/Users/jehyu/OneDrive/문서/github/python/pygame_basic/mob.png") 
mob_size = mob.get_rect().size # 이미지 크기를 구해옴
mob_width = mob_size[0]
mob_height = mob_size[0]
mob_x_pos = (screen_width / 2) - (mob_width / 2)
mob_y_pos = (screen_height / 2) - (mob_height / 2)

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()

#이벤트 루프
running = True
while running:
    dt = clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnuing = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    # 경계에 따른 처리  
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    # 몹과의 충돌
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    mob_rect = mob.get_rect()
    mob_rect.left = mob_x_pos
    mob_rect.top = mob_y_pos

    # 충돌 체크
    if character_rect.colliderect(mob_rect):
        print("충돌했어요")
        running = False
    
    
    screen.blit(background, (0,0)) # 배경 그리기
    
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(mob, (mob_x_pos, mob_y_pos))
    
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    # 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False
        
    pygame.display.update() # 게임화면을 다시 그리기 
# pygame 종료
pygame.quit()