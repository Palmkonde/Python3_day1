import pygame

class Circle:
    SCREEN_WIDTH = 100 
    SCREEN_HIGHT = 100 

    def __init__(self,
                 radius: int | float,
                 x: int | float, y: int | float) -> None:
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self) -> None:
        pygame.draw.circle(surface=screen, center=(self.x, self.y), color=(255, 255, 255), radius=5) 
        print(f"{self.x}, {self.y}")

    def move(self, forward: bool) -> bool:
        if self.x < self.SCREEN_WIDTH and self.y < self.SCREEN_HIGHT and forward:
            self.x += 1
            self.y += 1
            return True

        elif self.x <= 0 or self.y <= 0:
            return True

        elif self.x >= self.SCREEN_WIDTH or self.y >= self.SCREEN_HIGHT or not forward:
            self.x -= 1
            self.y -= 1
            return False

# setup pygame
pygame.init()
pygame.display.set_caption("Flying-circle")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((100, 100))

if __name__ == "__main__":
    circle = Circle(10, 100, 100)
    forward = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # reset screen
        screen.fill((0, 0, 0))

        # main game
        forward = circle.move(forward)
        circle.draw()
        
        # game update frame by frame
        pygame.display.update()
        clock.tick(60)