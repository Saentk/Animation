import pygame as p
from random import randint, choice, random
import math

class Circle:
    def __init__(self, screen, pos = (10,10), radius = 10):
        self.screen = screen
        self.color = (randint(0, 255),randint(0, 255),randint(0, 255))
        self.x, self.y = pos
        self.radius = radius
        self.speed_x = random() * choice([1,-1])
        self.speed_y = random() * choice([1,-1])
        self.screen_rect = screen.get_rect()
        self.move_type = 'bounce'

    def setup_circle(self):
        self.angle = random() * (math.pi * 2)
        self.circle_radious = randint(250, 300)
        self.angular_velocity = randint(1, 5) * 0.001
        self.center = (self.screen_rect.bottom / 2, self.screen_rect.right / 2)
        self.end_pos = (self.center[1] + self.circle_radious * math.cos(self.angle), 
            self.center[0] + self.circle_radious * math.sin(self.angle))
        self.num = randint(500, 1000)

    def check_edges(self):
        if self.x >= self.screen_rect.right or self.x <= self.screen_rect.left:
            self.speed_x *= -1
        if self.y >= self.screen_rect.bottom or self.y <= self.screen_rect.top:
            self.speed_y *= -1

    def update_bounce(self):
        self.check_edges()
        self.x += self.speed_x
        self.y += self.speed_y

        self.draw()

    def move_to_circle(self):
        self.get_distance()
        self.x += self.speed_x
        self.y += self.speed_y

        self. draw()

        if self.is_in_circle():
            self.move_type = 'circle'

    # distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    def get_distance(self):
        dx = self.end_pos[0] - self.x
        dy = self.end_pos[1] - self.y
        self.speed_x = dx / self.num
        self.speed_y = dy / self.num
        self.num -= 1

    def is_in_circle(self):
        return self.x == self.end_pos[0] and self.y == self.end_pos[1]

    def update_circle(self):
        self.angle += self.angular_velocity
        self.x = self.center[1] + self.circle_radious * math.cos(self.angle)
        self.y = self.center[0] + self.circle_radious * math.sin(self.angle)

        self.draw()

    def move(self):
        if self.move_type == 'bounce':
            self.update_bounce()
        elif self.move_type == 'form_circle':
            self.move_to_circle()
        elif self.move_type == 'circle':
            self.update_circle()

    def draw(self):
        p.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


