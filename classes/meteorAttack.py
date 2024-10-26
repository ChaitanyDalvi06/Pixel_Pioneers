import pygame
import math
from .constants import WIDTH, HEIGHT

class MeteorAttack(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, target_x, target_y, image):
        super().__init__()
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

        # Calculate the angle towards the target
        dx = target_x - start_x  # Difference in x
        dy = target_y - start_y  # Difference in y
        self.angle = math.degrees(math.atan2(dy, dx))  # Calculate angle in degrees

        # Set speed
        self.speed = 4

        # Calculate direction vector based on the angle
        self.direction_x = math.cos(math.radians(self.angle))
        self.direction_y = math.sin(math.radians(self.angle))

    def update(self):
        # Move the meteor based on the saved direction
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y

        # Rotate the meteor
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1)  # Rotate negatively to match the Pygame coordinate system
        self.rect = self.image.get_rect(center=self.rect.center)

        # Destroy if it goes out of bounds
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)