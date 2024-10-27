# #8_elements.py

class Water:
    def __add__(self, other):
        """
        Сложение воды с другими элементами для получения нового элемента.

        :param other: Другой элемент, с которым происходит сложение.
        :return: Новый элемент, полученный в результате сложения, или None, если сложение невозможно.
        """
        if isinstance(other, Air):
            return Storm()  # Вода + Воздух = Шторм
        elif isinstance(other, Fire):
            return Steam()  # Вода + Огонь = Пар
        elif isinstance(other, Earth):
            return Mud()    # Вода + Земля = Грязь
        return None


class Air:
    def __add__(self, other):
        """
        Сложение воздуха с другими элементами для получения нового элемента.

        :param other: Другой элемент, с которым происходит сложение.
        :return: Новый элемент, полученный в результате сложения, или None, если сложение невозможно.
        """
        if isinstance(other, Fire):
            return Lightning()  # Воздух + Огонь = Молния
        elif isinstance(other, Earth):
            return Dust()      # Воздух + Земля = Пыль
        return None


class Fire:
    def __add__(self, other):
        """
        Сложение огня с другими элементами для получения нового элемента.

        :param other: Другой элемент, с которым происходит сложение.
        :return: Новый элемент, полученный в результате сложения, или None, если сложение невозможно.
        """
        if isinstance(other, Earth):
            return Lava()  # Огонь + Земля = Лава
        return None


class Earth:
    def __add__(self, other):
        """
        Сложение земли с другими элементами для получения нового элемента.

        :param other: Другой элемент, с которым происходит сложение.
        :return: Новый элемент, полученный в результате сложения, или None, если сложение невозможно.
        """
        if isinstance(other, Water):
            return Mud()  # Земля + Вода = Грязь
        return None


class Storm:
    def __str__(self):
        """Возвращает строку "Шторм"."""
        return "Storm"  # Возвращает строку "Шторм"


class Steam:
    def __str__(self):
        """Возвращает строку "Пар"."""
        return "Steam"  # Возвращает строку "Пар"


class Mud:
    def __str__(self):
        """Возвращает строку "Грязь"."""
        return "Mud"  # Возвращает строку "Грязь"


class Lightning:
    def __str__(self):
        """Возвращает строку "Молния"."""
        return "Lightning"  # Возвращает строку "Молния"


class Dust:
    def __str__(self):
        """Возвращает строку "Пыль"."""
        return "Dust"  # Возвращает строку "Пыль"


class Lava:
    def __str__(self):
        """Возвращает строку "Лава"."""
        return "Lava"  # Возвращает строку "Лава"


# Пример использования
if __name__ == "__main__":
    print(Water() + Fire())  # Вывод: Steam
    print(Air() + Earth())    # Вывод: Dust
    print(Earth() + Water())  # Вывод: Mud
