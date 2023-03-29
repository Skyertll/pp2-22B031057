import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")

ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_speed = 20

ball_color = (255, 0, 0)
ball_radius = 25

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_pos[1] = max(ball_pos[1] - ball_speed, ball_radius)
            elif event.key == pygame.K_DOWN:
                ball_pos[1] = min(ball_pos[1] + ball_speed, SCREEN_HEIGHT - ball_radius)
            elif event.key == pygame.K_LEFT:
                ball_pos[0] = max(ball_pos[0] - ball_speed, ball_radius)
            elif event.key == pygame.K_RIGHT:
                ball_pos[0] = min(ball_pos[0] + ball_speed, SCREEN_WIDTH - ball_radius)
    

    screen.fill((255, 255, 255)) 
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    

    pygame.display.update()

pygame.quit()