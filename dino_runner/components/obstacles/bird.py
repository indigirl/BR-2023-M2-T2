import random

from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle

BIRD_HEIGHTS = [250, 290, 300]


class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0)
        self.rect.y = random.choice(BIRD_HEIGHTS)
        self.step_index = 0

    def draw(self, screen):        
        screen.blit(self.image[self.step_index//5], self.rect)
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0

 # // pega apenas o primeiro numero inteiro, sem os decimais
 #Até 5 o resultado da divisao é 0, a primeira imagem é passada = BIRD[0]
 #De 5 até 9 o resultado da divisão é 1, a segunda imagem é passada = BIRD [1]