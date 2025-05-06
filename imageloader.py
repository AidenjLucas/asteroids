import pygame


def loadimage(img,self):

    self.image = pygame.image.load(f"{img}").convert_alpha()
    self.image = pygame.transform.scale(self.image,(self.radius*2,self.radius*2))
    self.rect = self.image.get_rect(center=self.position)
