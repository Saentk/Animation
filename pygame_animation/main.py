import pygame as p
from random import randint
from circle import Particle
from button import Button

# Constants
CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 700
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 50
BUTTON_SPACING = 500
PARTICLE_SPACING = 10
BUTTON_POSITIONS = [(10, 10), (10 + BUTTON_SPACING, 10), (10 + 2 * BUTTON_SPACING, 10)]
BUTTON_TEXTS = ["Circle", "Triangle", "Square"]

def init_pygame():
    p.init()
    screen = p.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    p.display.set_caption("Pygame animation")
    return screen

def create_particles():
    return [Particle(screen, (randint(15, CANVAS_WIDTH - 15), randint(15, CANVAS_HEIGHT - 15)))
            for _ in range(1, CANVAS_HEIGHT // PARTICLE_SPACING)]

def create_buttons():
    return [Button(screen, pos[0], pos[1], BUTTON_WIDTH, BUTTON_HEIGHT, text)
            for pos, text in zip(BUTTON_POSITIONS, BUTTON_TEXTS)]

def game_loop(screen, buttons, particles):
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

            for button in buttons:
                button.handle_event(event, particles)

        screen.fill((255, 255, 255))

        for button in buttons:
            button.draw()

        for particle in particles:
            particle.move()

        p.display.flip()


screen = init_pygame()
particles = create_particles()
buttons = create_buttons()
game_loop(screen, buttons, particles)

p.quit()
