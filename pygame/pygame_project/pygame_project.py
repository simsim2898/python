import os
import pygame

pygame.init()

#size
screen_width = 640
screen_hight = 480
screen = pygame.display.set_mode((screen_width, screen_hight))

pygame.display.set_caption("test")

clock = pygame.time.Clock()

current_file = os.path.dirname(__file__)
image_file = os.path.join(current_file, "image")

# 일단 배경
background = pygame.image.load(os.path.join(image_file, "background.png"))

# 스테이지 
stage = pygame.image.load(os.path.join(image_file, "background3.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터
character = pygame.image.load(os.path.join(image_file, "ch.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_hight = character_size[1]
character_x_x = (screen_width / 2) - (character_width / 2)
character_y_y = screen_hight - character_hight - stage_height

# 캐릭터 이동
character_to_x = 0
character_speed = 5

# 무기
weapon = pygame.image.load(os.path.join(image_file, "we.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapons = []
weapon_speed = 10

# 나타 내기
run = True
while run:
    dt = clock.tick(30)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_x = character_x_x + (character_width / 2) - (weapon_width / 2)
                weapon_y_y = character_y_y
                weapons.append([weapon_x_x, weapon_y_y])
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

# 캐릭터 위치 설정
    character_x_x += character_to_x

    if character_x_x < 0:
        character_x_x = 0
    elif character_x_x > screen_width - character_width:
        character_x_x = screen_width - character_width
        
    # 무기 
    weapons = [ [w[0], w[1]- weapon_speed] for w in weapons]
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
        
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_hight - stage_height))
    screen.blit(character, (character_x_x, character_y_y))
    
    for weapon_x_x, weapon_y_y in weapons:
        screen.blit(weapon, (weapon_x_x, weapon_y_y))
    
    pygame.display.update()
pygame.quit()