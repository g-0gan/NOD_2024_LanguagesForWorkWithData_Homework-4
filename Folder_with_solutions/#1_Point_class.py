class Point:
    def __init__(self, x, y):
        """
        Инициализирует объект точки с заданными координатами.

        :param x: Координата x точки.
        :param y: Координата y точки.
        """
        self.x = x
        self.y = y


# Пример использования
if __name__ == "__main__":
    point = Point(3, 4)
    print(f"Point coordinates: ({point.x}, {point.y})")
