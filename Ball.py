

class Ball():

    def __init__(self, pygame=None, radius=10, color=(255, 255, 255), x=0, y=0, xspeed=1, yspeed=1):
        self.pygame = pygame
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed

    def check_collision(self, paddle):
        if self.x - self.radius <= paddle.x + paddle.width and paddle.y <= self.y <= paddle.y + paddle.height:
            self.xspeed = -self.xspeed

    def draw(self, screen):
        self.pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed

        if self.x > 800 or self.x < 0:
            self.xspeed = -self.xspeed
        if self.y > 600 or self.y < 0:
            self.yspeed = -self.yspeed

