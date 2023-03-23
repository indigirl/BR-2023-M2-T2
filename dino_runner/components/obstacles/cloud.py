import random

from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(100, 300)
        self.image = CLOUD
        self.rect = self.image.get_rect()

    def update(self, game_speed):
        self.x -= game_speed
        if self.x < self.rect.width:
            self.x = SCREEN_WIDTH + random.randint(800, 1000)
            self.y = random.randint(100, 300)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))