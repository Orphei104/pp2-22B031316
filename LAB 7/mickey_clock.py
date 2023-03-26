import pygame
import datetime

pygame.init()
width = 800
height = 600
angle1 = 0
angle2 = 0

pygame.mixer.music.load("pygame_data\\Nujabes - Aruarian Dance.mp3")
pygame.mixer.music.play(-1)

font = pygame.font.Font('pygame_data/NanumGothicCoding-Bold.ttf',30)
monitor = pygame.display.set_mode((width,height),pygame.RESIZABLE)

pygame.display.set_caption("simple clock")
pygame.display.set_icon(pygame.image.load("pygame_data\pentagon_icon.png"))

monitor.fill((255,255,255))

mickey_surf = pygame.image.load("pygame_data\mickeyclock.jpg")
left_hand_surf = pygame.image.load("pygame_data\left_hand.png").convert_alpha()
right_hand_surf = pygame.image.load("pygame_data/right_hand.png").convert_alpha()

mickey_surf = pygame.transform.scale( mickey_surf ,(mickey_surf.get_width()//2.7 , mickey_surf.get_height()//2.7))

x=0
while 1:
    t = datetime.datetime.now()
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            pygame.quit()
    angle1 = -datetime.datetime.now().second
    angle2 = -t.minute * 6

    sc_f_sys = font.render(f'{t:%H-%M-%S}', 1 , (0,0,0),(255,255,255))
    
    left_hand_surf1 = pygame.transform.rotate(left_hand_surf,x)
    right_hand_surf1 = pygame.transform.rotate(right_hand_surf,angle2)
    
    right_hand_surf1=pygame.transform.scale(right_hand_surf1,(right_hand_surf1.get_width()//1.2 ,right_hand_surf1.get_height()//1.5))
    left_hand_surf1=pygame.transform.scale(left_hand_surf1,(left_hand_surf1.get_width()//1.2 , left_hand_surf1.get_height()//1.5))
    
    mickeyrect = mickey_surf.get_rect(center = (width//2,height//2))
    left_hand_rect = left_hand_surf1.get_rect(center = (width//2,height//2))
    right_hand_rect = right_hand_surf1.get_rect(center = (width//2,height//2))
    
    monitor.blit(mickey_surf,mickeyrect)
    monitor.blit(left_hand_surf1,left_hand_rect)
    monitor.blit(right_hand_surf1,right_hand_rect)
    monitor.blit(sc_f_sys,(10,10))    
    x-=6
    pygame.display.update()

    pygame.time.delay(1000)  