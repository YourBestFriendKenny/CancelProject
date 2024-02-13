import pygame 


def Music():
    pygame.init()
    song = pygame.mixer.Sound('./Lol.mp3')
    clock = pygame.time.Clock()
    song.play()
    while True:
        clock.tick(60)
    pygame.quit()

