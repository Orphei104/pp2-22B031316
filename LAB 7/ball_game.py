import pygame
pygame.init()
monitor = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Draw Circle")
ball_radius = 25
ball_position = [640 // 2, 480 // 2]
ball_speed = 20
ball_color = (255, 0, 0)
clock = pygame.time.Clock()
check = True

while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_position[1] -= ball_speed
            elif event.key == pygame.K_DOWN:
                ball_position[1] += ball_speed
            elif event.key == pygame.K_LEFT:
                ball_position[0] -= ball_speed
            elif event.key == pygame.K_RIGHT:
                ball_position[0] += ball_speed
    
    ball_position[0] = max(ball_position[0], ball_radius)
    ball_position[0] = min(ball_position[0], 640 - ball_radius)
    ball_position[1] = max(ball_position[1], ball_radius)
    ball_position[1] = min(ball_position[1], 480 - ball_radius)
    monitor.fill((255, 255, 255))
    pygame.draw.circle(monitor, ball_color, ball_position, ball_radius)
    pygame.display.flip()
    clock.tick(60)