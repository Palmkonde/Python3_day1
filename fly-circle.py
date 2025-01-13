class Circle:
    def __init__(self,
                 radius: int | float,
                 x: int | float, y: int | float) -> None:
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self) -> None:
        print(f"{self.x}, {self.y}")

    def move(self) -> None:
        self.x += 1
        self.y += 1


if __name__ == "__main__":
    circle = Circle(10, 100, 100)
    circle.draw()
