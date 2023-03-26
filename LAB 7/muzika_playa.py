import pygame
pygame.init()
monitor = pygame.display.set_mode((1280, 720))
playlist = ["pygame_data/Skryptonite - Animals Remix.mp3", "pygame_data/Nujabes - Aruarian Dance.mp3", "pygame_data/KUTE x RAIZHELL - Anubis.mp3"]
current_song_index = 0
pygame.mixer.music.load(playlist[current_song_index])
pygame.mixer.music.play()
check = True

while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song_index])
                pygame.mixer.music.play()

    monitor.fill((255,255,255))
    current_song = playlist[current_song_index].split('/')[-1].replace('.mp3','')
    font = pygame.font.Font('pygame_data/NanumGothicCoding-Bold.ttf', 50)
    name = font.render(current_song, True, (0, 0, 0))
    name_to_the_center = name.get_rect(center = monitor.get_rect().center)
    monitor.blit(name, name_to_the_center)

    pygame.display.update()
    pygame.display.flip()