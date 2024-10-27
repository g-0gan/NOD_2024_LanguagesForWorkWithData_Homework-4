class Point:
    def __init__(self, x, y):
        """
        Инициализирует объект точки с заданными координатами.

        :param x: Координата x точки.
        :param y: Координата y точки.
        """
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, bottom_left, top_right):
        """
        Инициализирует объект прямоугольника с заданными углами.

        :param bottom_left: Объект Point, представляющий нижний левый угол прямоугольника.
        :param top_right: Объект Point, представляющий верхний правый угол прямоугольника.
        """
        self.bottom_left = bottom_left
        self.top_right = top_right

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        :return: Площадь прямоугольника.
        """
        width = self.top_right.x - self.bottom_left.x
        height = self.top_right.y - self.bottom_left.y
        return width * height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        :return: Периметр прямоугольника.
        """
        width = self.top_right.x - self.bottom_left.x
        height = self.top_right.y - self.bottom_left.y
        return 2 * (width + height)


# Пример использования
if __name__ == "__main__":
    rect = Rectangle(Point(1, 1), Point(5, 5))
    print("Area:", rect.area())
    print("Perimeter:", rect.perimeter())
