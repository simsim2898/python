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
stage = pygame.image.load(os.path.join(image_file, "background2.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터
character = pygame.image.load(os.path.join(image_file, "ch.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_hight = character_size[1]
character_x_x = (screen_width / 2) - (character_width / 2)
character_y_y = screen_hight - character_hight - stage_height

# 나타 내기
run = True
while run:
    dt = clock.tick(60)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_hight - stage_height))
    screen.blit(character, (character_x_x, character_y_y))
    
    pygame.display.update()
pygame.quit()