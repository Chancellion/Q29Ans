from abc import ABC, abstractmethod
import math
from typing import List

input("Виконав Іванченко Даніїл, КІб-1-23-4.0д")

class IDrawable(ABC):
    """Формальний «інтерфейс» для всього, що можна намалювати."""
    
    @abstractmethod
    def draw(self) -> None:
        """Виводить на екран якийсь примітивний ASCII-малюнок."""
        pass

class Shape(ABC):
    """Базова фігура з обов’язковим методом обчислення площі."""
    
    @abstractmethod
    def calculate_area(self) -> float:
        """Повертає площу фігури."""
        pass

#===================================================

class Circle(Shape, IDrawable):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius ** 2

    def draw(self) -> None:
        print("(•‿•)  ← умовне коло")


class Square(Shape, IDrawable):
    def __init__(self, side: float) -> None:
        self.side = side

    def calculate_area(self) -> float:
        return self.side ** 2

    def draw(self) -> None:
        print("┌─┐\n│ │  ← умовний квадрат\n└─┘")


class Triangle(Shape, IDrawable):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        return 0.5 * self.base * self.height

    def draw(self) -> None:
        print(" /\\\n/__\\  ← умовний трикутник")

def main() -> None:
    shapes: List[Shape] = [
        Circle(radius=3),
        Square(side=4),
        Triangle(base=5, height=2),
    ]

    for shp in shapes:
        # у цьому циклі Python сприймає їх як об'єкти Shape, але викликає «правильний» метод конкретного класу
        area = shp.calculate_area()
        print(f"{shp.__class__.__name__}: area = {area:.2f}")
        if isinstance(shp, IDrawable):
            shp.draw()
        print("-" * 20)


if __name__ == "__main__":
    main()
