import pygame


def loadImage(imapath,transparent=True):
    img = pygame.image.load(imapath)
    img=img.convert()
    if transparent:
        color= img.get_at((0,0))
        img.set_colorkey(color,pygame.RLEACCEL)
    return img