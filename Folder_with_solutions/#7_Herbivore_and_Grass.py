class Grass:
    def __init__(self, nutrition_value):
        """
        Инициализирует объект Grass с заданным значением питательной ценности.

        :param nutrition_value: Питательная ценность травы.
        """
        self.nutrition_value = nutrition_value


class Herbivore:
    def __init__(self):
        """
        Инициализирует объект Herbivore с начальным уровнем голода.
        """
        self.hunger = 10  # начальный уровень голода

    def eat(self, food):
        """
        Позволяет травоядному поесть пищу, уменьшая уровень голода.

        :param food: Объект, представляющий пищу (например, Grass).
        :return: Строка, указывающая на состояние (поедание пищи или отсутствие голода).
        """
        if self.hunger > 0:
            self.hunger -= food.nutrition_value
            return "Eating grass"
        return "Not hungry"


# Пример использования
if __name__ == "__main__":
    grass = Grass(3)
    herbivore = Herbivore()
    print("Hunger before eating:", herbivore.hunger)
    print(herbivore.eat(grass))
    print("Hunger after eating:", herbivore.hunger)
