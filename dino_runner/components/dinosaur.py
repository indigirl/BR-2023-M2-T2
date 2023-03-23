import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, HAMMER_TYPE, DUCKING_HAMMER, JUMPING_HAMMER, RUNNING_HAMMER, MUSHROOM_TYPE, RUNNING_BIG, DUCKING_BIG, JUMPING_BIG, HEART_TYPE

DUCK_IMG = {DEFAULT_TYPE: DUCKING, HEART_TYPE: DUCKING, SHIELD_TYPE:DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, MUSHROOM_TYPE: DUCKING_BIG}
RUN_IMG =  {DEFAULT_TYPE: RUNNING, HEART_TYPE: RUNNING, SHIELD_TYPE:RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, MUSHROOM_TYPE: RUNNING_BIG}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, HEART_TYPE: JUMPING, SHIELD_TYPE:JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, MUSHROOM_TYPE: JUMPING_BIG}

X_POS = 80
Y_POS = 310
Y_POS_DUCK = 340
Y_POS_BIG = 290 
Y_POS_DUCK_BIG = 320
JUMP_VEL = 8.5


class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.dino_jump = False
        self.dino_run = True
        self.dino_ducking = False
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.show_text = False
        self.power_up_time = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_ducking:
            self.duck()

        if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE]) and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_ducking = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_ducking = True
        elif not self.dino_jump and not self.dino_ducking:
            self.dino_jump = False
            self.dino_run = True
            self.dino_ducking = False
        
        if self.step_index >= 9:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS if self.type != "mushroom" else Y_POS_BIG
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        
        if self.jump_vel <-JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK if self.type != "mushroom" else Y_POS_DUCK_BIG
        self.step_index += 1
        self.dino_ducking = False
        
    def draw(self, screen):
        screen.blit(self.image,(self.dino_rect.x, self.dino_rect.y))
