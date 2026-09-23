import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fire Effect")

clock = pygame.time.Clock()

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(3, 7)
        self.color = (random.randint(200, 255), random.randint(100, 150), 0)  # orange/yellow
        self.speed_y = random.uniform(-2, -5)  # upward
        self.speed_x = random.uniform(-1, 1)   # sideways drift
        self.alpha = 255

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.size = max(0, self.size - 0.1)
        self.alpha -= 3

    def draw(self, surface):
        if self.alpha > 0 and self.size > 0:
            s = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (*self.color, int(self.alpha)), (self.size, self.size), int(self.size))
            surface.blit(s, (self.x, self.y))

particles = []

# Main loop
while True:
    screen.fill((0, 0, 0))  # black background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Spawn new particles
    particles.append(Particle(WIDTH//2, HEIGHT-50))

    # Update and draw particles
    for p in particles[:]:
        p.update()
        p.draw(screen)
        if p.alpha <= 0 or p.size <= 0:
            particles.remove(p)

    pygame.display.flip()
    clock.tick(60)