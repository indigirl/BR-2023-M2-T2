import random
import pygame

from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE, MUSHROOM_TYPE
from dino_runner.components.power_ups.power_up_chooser import RandomPowerUp


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and (self.when_appears == score):
            self.when_appears += random.randint(200, 300)
            self.type = 0
            self.power_up = [RandomPowerUp()]
            self.power_ups.append(self.power_up[self.type])                                                #
    
    def update(self, score, game_speed, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                if power_up.type == HAMMER_TYPE:
                    player.hammer = True
                    player.shield = False
                    player.mushroom = False
                elif power_up.type == SHIELD_TYPE:
                    player.hammer = False
                    player.shield = True
                    player.mushroom = False
                elif power_up.type == MUSHROOM_TYPE:
                    player.hammer = False
                    player.shield = True
                    player.mushroom = True
                
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)

    