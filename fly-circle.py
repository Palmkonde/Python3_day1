import pygame
from random import randint
from typing import Self

# Constant variables
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600

class Circle:
    def __init__(self,
                 radius: int | float,
                 x: int | float, y: int | float,
                 vx: int | float, vy: int | float) -> None:
        self.radius = radius
        self.x = x
        self.y = y
        
        self.vx = vx
        self.vy = vy

    def draw(self) -> None:
        pygame.draw.circle(surface=screen, center=(
            self.x, self.y), color=(255, 255, 255), radius=self.radius)

    def check_collision_with(self, other: Self) -> None:
        distance = ((self.x - other.x)**2 + (self.y - other.y)**2)**(1/2)
        
        if distance < (self.radius + other.radius):
            # overlap means r1 + r2 < distance
            overlap = (self.radius + other.radius) - distance
            
            # Normalize dx, dy to 1 because we want only its direction
            dx = (self.x - other.x) / distance
            dy = (self.y - other.y) / distance

            # to avoid intersection 
            self.x += dx * (overlap / 2)
            self.y += dy * (overlap / 2)
            
            other.x -= dx * (overlap / 2)
            other.y -= dy * (overlap / 2)

            # Swaap velocity of self and other object
            self.vx, other.vx = other.vx, self.vx
            self.vy, other.vy = other.vy, self.vy

    def check_collision(self) -> None:
        if self.x + self.radius > SCREEN_WIDTH or self.x - self.radius < 0:
            self.vx = -self.vx

        if self.y + self.radius > SCREEN_HIGHT or self.y - self.radius < 0:
            self.vy = -self.vy

    def move(self) -> bool:
        self.check_collision()
        self.x += self.vx
        self.y += self.vy


# setup pygame
pygame.init()
pygame.display.set_caption("Flying-circle")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

if __name__ == "__main__":
    # circle = Circle(15, 100, 100, 5, 5)
    # circle2 = Circle(25, 50, 50, 2, 3)
    # circle3 = Circle(12, 20, 20, 4, 5)
    # circle4 = Circle(9, 400, 300, 6, 6)

    # circle_group = [circle, circle2, circle3, circle4] 
    
    N = 10
    circle_group = []
    for i in range(N):
        size = randint(5, 25)
        centerx = randint(50, SCREEN_WIDTH - 50)
        centery = randint(50, SCREEN_HIGHT - 50)
        vx = randint(1, 5)
        vy = randint(1, 5)

        circle_group.append(Circle(size, centerx, centery, vx, vy))

    # Main game
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # reset screen
        screen.fill((0, 0, 0))

        for i in range(len(circle_group)):
            for j in range(i+1, len(circle_group)):
                circle_group[i].check_collision_with(circle_group[j])
        
        # move circles around
        for c in circle_group:
            c.move()
            c.draw()

        # game update frame by frame
        pygame.display.update()
        clock.tick(60)
