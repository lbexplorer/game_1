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
            self.speed += 1
            scores = [0, 0]
            hit_sound.play()
        # 撞上上侧的墙
        elif self.rect.top == 0:
            self.direction_y = 1
            self.speed += 1
            scores = [0, 0]
        # 撞上下侧的墙
        elif self.rect.top == self.cfg.HEIGHT - self.rect.height:
            self.direction_y = -1
            self.speed += 1
        # 撞上左边的墙
        elif self.rect.left < 0:
            self.reset()
            racket_left.reset()
            racket_right.reset()
            scores = [0, 1]
            goal_sound.play()
        # 撞上右边的墙
        elif self.rect.right > self.cfg.WIDTH:
            self.reset()
            racket_left.reset()
            racket_right.reset()
            scores = [1, 0]
            goal_sound.play()
        # 普通情况
        else:
            scores = [0, 0]
        return scores

    """初始化"""

    def reset(self):
        self.rect.centerx = self.cfg.WIDTH // 2
        self.rect.centery = random.randrange(self.rect.height // 2, self.cfg.HEIGHT - self.rect.height // 2)
        self.direction_x = random.choice([1, -1])
        self.direction_y = random.choice([1, -1])
        self.speed = 1

    """绑定到屏幕上"""

    def draw(self, screen):
        screen.blit(self.image, self.rect)
