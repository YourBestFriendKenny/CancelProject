import pygame 


def Music1():
    pygame.init()
    song = pygame.mixer.Sound('./BadBlood.mp3')
    clock = pygame.time.Clock()
    song.play()
    while True:
        clock.tick(60)
    pygame.quit()



def Music2():
    pygame.init()
    song = pygame.mixer.Sound('./Lol.mp3')
    clock = pygame.time.Clock()
    song.play()
    while True:
        clock.tick(60)
    pygame.quit()


