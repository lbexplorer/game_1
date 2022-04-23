import pygame


def Button(screen, position, text, button_size=(200, 50)):
    left, top = position
    bwidth, bheight = button_size
    pygame.draw.line(screen, (150, 150, 150), (left, top), (left + bwidth, top), 5)
    pygame.draw.line(screen, (150, 150, 150), (left, top - 2), (left, top + bwidth), 5)
    pygame.draw.line(screen, (50, 50, 50), (left, top + bheight), (left + bwidth, top + bheight), 5)
    pygame.draw.line(screen, (50, 50, 50), (left + bwidth, top + bheight), (left + bwidth, top), 5)
    pygame.draw.rect(screen, (100, 100, 100), (left, top, bwidth, bheight))


def startlnterface(screen):
    clock = pygame.time.Clock()
    while True:
        screen.fill((41, 36, 33))
        button_1 = Button()


if __name__ == '__main__':
    pass
