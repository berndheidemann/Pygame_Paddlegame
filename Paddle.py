
class Paddle:

    def __init__(self, pygame=None, x=200, y=200, width=10, height=60, color=(255, 255, 255), speed=5):
        self.pygame = pygame
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def draw(self, screen):
        keys = self.pygame.key.get_pressed()
        if keys[self.pygame.K_UP]:
            self.move_up()

        if keys[self.pygame.K_DOWN]:
            self.move_down()

        self.pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move_up(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 0

    def move_down(self):
        self.y += self.speed
        if self.y > 600 - self.height:
            self.y = 600 - self.height