import pygame as p
from random import randint, choice
from circle import Circle
from button import Button

# Initialize pygame
p.init()

# Canvas
canvas_width = 1200
canvas_height = 700

screen = p.display.set_mode((canvas_width, canvas_height))
p.display.set_caption("Pygame animation")

# Particles
lst = []
for i in range(1, canvas_height//10):
    obj = Circle(screen, (randint(15, canvas_width - 15),randint(15, canvas_height - 15)))
    lst.append(obj)
# Buttons
buttons = []
button_positions = [(10, 10), (200, 10), (390, 10)]
button_texts = ["Circle", "Triangle", "Square"]

for pos, text in zip(button_positions, button_texts):
    button = Button(screen, pos[0], pos[1], 120, 50, text)
    buttons.append(button)

# Main game loop
running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for button in buttons:
        button.handle_event(event, lst)
        button.draw()

    for i in lst:
        i.move()

    p.display.flip()

p.quit()
