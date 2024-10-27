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

    def contains(self, point):
        """
        Проверяет, содержится ли заданная точка внутри прямоугольника.

        :param point: Объект Point, который нужно проверить на принадлежность к прямоугольнику.
        :return: True, если точка находится внутри прямоугольника; False в противном случае.
        """
        return (self.bottom_left.x <= point.x <= self.top_right.x and
                self.bottom_left.y <= point.y <= self.top_right.y)


# Пример использования
if __name__ == "__main__":
    rect = Rectangle(Point(1, 1), Point(5, 5))
    point_inside = Point(3, 3)
    point_outside = Point(6, 6)
    print("Point inside:", rect.contains(point_inside))   # True
    print("Point outside:", rect.contains(point_outside))  # False
