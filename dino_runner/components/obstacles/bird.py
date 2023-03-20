import random

from dino_runner.components.obstacles.obstacle import Obstacle

BIRD_HEIGHTS = [250, 290]


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0              #o tipo é apenas um, animado
        super().__init__(image, self.type)
        self.rect.y = random.choice(BIRD_HEIGHTS)
        self.step_index = 0

    def draw(self, screen):
        if self.step_index >= 9:
            self.step_index = 0
        
        screen.blit(self.image[self.step_index//5], self.rect)
        self.step_index += 1

 #caminho da imagem ObstacleManager> obstacle> bird
 #O Tipo será passado após a divisão, // pega apenas o primeiro numero inteiro, sem os decimais
 #Até 5 o resultado da divisao é 0, a primeira imagem é passada = BIRD[0]
 #De 5 até 9 o resultado da divisão é 1, a segunda imagem é passada = BIRD [1]