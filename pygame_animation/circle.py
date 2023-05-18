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
        self.center = (self.screen_rect.right / 2, self.screen_rect.bottom / 2)
        self.move_type = 'bounce'

    def setup_circle(self):
        self.angle = random() * (math.pi * 2)
        self.circle_radious = randint(250, 300)
        self.angular_velocity = randint(1, 5) * 0.001
        self.end_pos = (self.center[0] + self.circle_radious * math.cos(self.angle), 
            self.center[1] + self.circle_radious * math.sin(self.angle))
        self.num = randint(500, 1000)
        self.final_form = 'circle'

    def setup_triangle(self):
        self.side = math.floor(random() * 3)
        self.progress = random()
        self.speed = random() * 0.001
        self.triangle_radius = randint(200, 250);
        self.vertices = [(self.center[0], self.center[1] - self.triangle_radius),
                        (self.center[0] + self.triangle_radius * math.sin(math.pi / 3), self.center[1] + self.triangle_radius / 2),
                        (self.center[0] - self.triangle_radius * math.sin(math.pi / 3), self.center[1] + self.triangle_radius / 2)]
        self.end_pos = self.get_triangle_point(self.side, self.progress)
        self.num = randint(500, 1000)
        self.final_form = 'triangle'

    def setup_square(self):
        self.side = randint(0, 3)
        self.progress = random()
        self.speed = random() * 0.001
        self.square_size = randint(250, 300)
        self.points = self.set_square_sides()
        self.end_pos = self.getSquarePoint(self.side, self.progress)
        self.num = randint(500, 1000)
        self.final_form = 'square'

    def set_square_sides(self):
        half_size = self.square_size / 2
        topLeft = (self.center[0] - half_size, self.center[1] - half_size)
        topRight = (self.center[0] + half_size, self.center[1] - half_size)
        bottomLeft = (self.center[0] - half_size, self.center[1] + half_size)
        bottomRight = (self.center[0] + half_size, self.center[1] + half_size)

        points = [topLeft, topRight, bottomRight, bottomLeft]
        return points

    def getSquarePoint(self, side, progress):

        start = self.points[side]
        end = self.points[(side + 1) % 4]

        x = self.lerp(start[0], end[0], progress)
        y = self.lerp(start[1], end[1], progress)

        return (x, y)

    def get_triangle_point(self, side, progress):
        start = self.vertices[side]
        end = self.vertices[(side + 1) % 3]

        x = self.lerp(start[0], end[0], progress)
        y = self.lerp(start[1], end[1], progress)

        return (x,y)

    def lerp(self, start, end, progress):
        return start + (end - start) * progress

    def check_edges(self):
        if self.x >= self.screen_rect.right or self.x <= self.screen_rect.left:
            self.speed_x *= -1
        if self.y >= self.screen_rect.bottom or self.y <= self.screen_rect.top:
            self.speed_y *= -1

    def update_bounce(self):
        self.check_edges()
        self.x += self.speed_x
        self.y += self.speed_y

    def update_circle(self):
        self.angle += self.angular_velocity
        self.x = self.center[0] + self.circle_radious * math.cos(self.angle)
        self.y = self.center[1] + self.circle_radious * math.sin(self.angle)

    def update_triangle(self):
        self.progress += self.speed
        if self.progress >= 1:
            self.progress = 0
            self.side = (self.side + 1) % 3

        self.x, self.y = self.get_triangle_point(self.side, self.progress)

    def update_square(self):
        self.progress += self.speed
        if self.progress >= 1:
            self.progress = 0
            self.side = (self.side + 1) % 4
        self.x, self.y = self.getSquarePoint(self.side, self.progress)

    def move_to_position(self):
        self.get_distance()
        self.x += self.speed_x
        self.y += self.speed_y

        if self.is_in_position():
            self.move_type = self.final_form

    def is_in_position(self):
        return self.x == self.end_pos[0] and self.y == self.end_pos[1]

    # distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    def get_distance(self):
        dx = self.end_pos[0] - self.x
        dy = self.end_pos[1] - self.y
        self.speed_x = dx / self.num
        self.speed_y = dy / self.num
        self.num -= 1

    def move(self):
        if self.move_type == 'bounce':
            self.update_bounce()
        elif self.move_type == 'to_position':
            self.move_to_position()
        elif self.move_type == 'circle':
            self.update_circle()
        elif self.move_type == 'triangle':
            self.update_triangle()
        elif self.move_type == 'square':
            self.update_square()

        self.draw()

    def draw(self):
        p.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


