import pygame

#initialize required modules
pygame.init()

#setup window geometry
screen = pygame.display.set_mode((400,500))

while True:
    #clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #make changes visible
    pygame.display.flip()