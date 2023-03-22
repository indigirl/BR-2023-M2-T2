import random

from dino_runner.utils.constants import SHIELD, SHIELD_TYPE, HAMMER, HAMMER_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

POWER_OPTIONS = [
    (SHIELD, SHIELD_TYPE),
    (HAMMER, HAMMER_TYPE),
    ]

class RandomPowerUp(PowerUp):
    def __init__(self):
        self.image, self.type = POWER_OPTIONS[random.randint(0,1)]
        super().__init__(self.image, self.type)