import pygame

class Circle:
    SCREEN_WIDTH = 800
    SCREEN_HIGHT = 600

    def __init__(self,
                 radius: int | float,
                 x: int | float, y: int | float) -> None:
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self) -> None:
        pygame.draw.circle(surface=screen, center=(
            self.x, self.y), color=(255, 255, 255), radius=self.radius)
        print(f"{self.x}, {self.y}")

    def move(self, vx: int, vy: int) -> bool:
        self.x += vx
        self.y += vy


# setup pygame
pygame.init()
pygame.display.set_caption("Flying-circle")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

if __name__ == "__main__":
    circle = Circle(10, 100, 100)

    # velocity
    vx, vy = 5, 5

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # reset screen
        screen.fill((0, 0, 0))

        # main game
        if circle.x > circle.SCREEN_WIDTH or circle.x < 0:
            vx = -vx

        if circle.y > circle.SCREEN_HIGHT or circle.y < 0:
            vy = -vy

        circle.move(vx, vy)
        circle.draw()

        # game update frame by frame
        pygame.display.update()
        clock.tick(60)
