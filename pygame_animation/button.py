import pygame as p

# Constants
FONT_SIZE = 24
ACTIVE_COLOR = (0, 255, 0)
INACTIVE_COLOR = (200, 200, 200)
TEXT_COLOR = (0, 0, 0)
BUTTON_ACTIVATION_DELAY = 500

class Button():
    def __init__(self, screen, x, y, w, h, text):
        self.screen = screen
        self.image = p.Surface((w, h))
        self.image.fill(ACTIVE_COLOR)
        font = p.font.Font(None, FONT_SIZE)
        self.text = text
        render_text = font.render(text, True, TEXT_COLOR)
        text_rect = render_text.get_rect(center=self.image.get_rect().center)
        self.image.blit(render_text, text_rect)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.active = True

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def handle_event(self, event, particles):
        if event.type == p.MOUSEBUTTONDOWN and self.active:
            mouse_pos = p.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.create_shape(particles)
                self.active = False
                p.time.set_timer(p.USEREVENT + 1, BUTTON_ACTIVATION_DELAY)
        elif event.type == p.USEREVENT + 1:
            self.active = True

    def create_shape(self, particles):
        shape_creation_map = {
            "Circle": self.setup_shape,
            "Triangle": self.setup_shape,
            "Square": self.setup_shape,
        }
        
        setup_function = shape_creation_map.get(self.text, None)
        if setup_function:
            setup_function(particles, self.text)

    def setup_shape(self, particles, shape_type):
        for particle in particles:
            if particle.move_type != 'to_position' and particle.move_type != shape_type.lower():
                getattr(particle, f"setup_{shape_type.lower()}")()
                particle.move_type = 'to_position'
            elif particle.move_type == shape_type.lower():
                particle.move_type = 'bounce'
