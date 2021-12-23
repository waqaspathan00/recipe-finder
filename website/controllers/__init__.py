import pygame

pygame.init()
clock = pygame.time.Clock()
screen_width =  # ENTER A VALUE HERE
screen_height =  # ENTER A VALUE HERE
screen = pygame.display.set_mode((screen_width, screen_height))

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    pygame.display.update()
    clock.tick(60)
