import pygame as p
from random import randint, choice
from circle import Circle
from button import Button

# Initialize pygame
p.init()

# Set the width and height of the canvas
canvas_width = 1200
canvas_height = 700

# Create the canvas (window) to draw on
screen = p.display.set_mode((canvas_width, canvas_height))

# Set the title of the window
p.display.set_caption("Blank Canvas")
lst = []
for i in range(1, canvas_height//10):
    obj = Circle(screen, (randint(15, canvas_width - 15),randint(15, canvas_height - 15)))
    lst.append(obj)

buttons = []

button_positions = [(10, 10), (200, 10), (390, 10)]  # Example positions
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

# Quit pygame
p.quit()
