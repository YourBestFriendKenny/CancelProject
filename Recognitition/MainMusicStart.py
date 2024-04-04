import pygame



def Music1():
    pygame.init()
    song = pygame.mixer.Sound('./Music/Eminem_-_The_Real_Slim_Shady_47829433.mp3')
    clock = pygame.time.Clock()
    song.play()
    while True:
        clock.tick(60)
    pygame.quit()




def Music2():
    pygame.init()
    song = pygame.mixer.Sound('./Music/Lol.mp3')
    clock = pygame.time.Clock()
    song.play()
    while True:
        clock.tick(60)
    pygame.quit()


