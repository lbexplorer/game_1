import random

import pygame as pygame

from game_main.utils import loadImage


class Ball(pygame.sprite.Sprite):
    def __init__(self, imgpath, cfg, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.cfg = cfg
        self.image = loadImage(imgpath)
        self.rect = self.image.get_rect()
        self.reset()

    """移动"""

    def move(self, ball, racket_left, racket_right, hit_sound, goal_sound):
        self.rect.left = self.rect.left + self.speed * self.direction_x
        self.rect.top = min(max(self.rect.top + self.speed * self.direction_y, 0), self.cfg.HEIGHT - self.rect.height)
        # 如果碰到球拍
        if pygame.sprite.collide_rect(ball, racket_left) or pygame.sprite.collide_rect(ball, racket_right):
            self.direction_x, self.direction_y = -self.direction_x, random.choice([1, -1])
