import pygame

pygame.init()
displayWidth = 800
displayHeight = 600
surface = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Image')
displayImage = pygame.image.load(r'D:\RESUMES\Raghu.jpg')
while True:

    surface.fill((255, 255, 255))
    surface.blit(displayImage, (0, 0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
