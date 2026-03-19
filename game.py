import pygame
import random

WIDTH = 800
HEIGHT = 600

class FallingEmoji:

    def __init__(self, emotions):

        self.emotion = random.choice(emotions)
        self.x = random.randint(50, WIDTH-50)
        self.y = 0
        self.speed = random.randint(3,6)

    def update(self):
        self.y += self.speed

    def draw(self, screen, emoji_images):

        img = emoji_images[self.emotion]
        screen.blit(img,(self.x,self.y))