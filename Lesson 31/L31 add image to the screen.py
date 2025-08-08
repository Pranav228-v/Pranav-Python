import pygame

#initalize required modules
pygame.init()
white = (160, 150, 70)

#clock
clock = pygame.time.Clock()

#creating the display surface object
#of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((500, 500))

#set the pygame window name
pygame.display.set_caption('Cat Image')

#creating a surface object, image is drawn on it.
image = pygame.image.load('Lesson 31/cat.jpg')

#set the size for the image
DEFAULT_IMAGE_SIZE = (200, 200)

#scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

#set a default position
DEFAULT_IMAGE_POSITION = (150,150)

#infinite loop
while True:
    display_surface.fill(white)
    display_surface.blit(image, DEFAULT_IMAGE_POSITION)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit the program
            quit()

    #part of event loop
    pygame.display.flip()
    clock.tick(30)