import pygame


def loadimage(img,object,flag=0):

    image = pygame.image.load(f"{img}").convert_alpha()
    image = pygame.transform.scale(image,(object.radius*2,object.radius*2))
    rect = image.get_rect(center=object.position)
    if flag == 0:
        return image,rect
    return image
    