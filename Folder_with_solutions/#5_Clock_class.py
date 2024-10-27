class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        """
        Инициализирует объект часов с заданным временем.

        :param hour: Часы (0-23), по умолчанию 0.
        :param minute: Минуты (0-59), по умолчанию 0.
        :param second: Секунды (0-59), по умолчанию 0.
        """
        self.hour = hour % 24
        self.minute = minute % 60
        self.second = second % 60

    def add_hour(self):
        """
        Увеличивает часы на 1.
        Если время превышает 23 часа, оно сбрасывается на 0.
        """
        self.hour = (self.hour + 1) % 24

    def add_minute(self):
        """
        Увеличивает минуты на 1.
        Если минуты достигают 60, они сбрасываются на 0 и вызывается метод для добавления часа.
        """
        if self.minute == 59:
            self.minute = 0
            self.add_hour()
        else:
            self.minute += 1

    def add_second(self):
        """
        Увеличивает секунды на 1.
        Если секунды достигают 60, они сбрасываются на 0 и вызывается метод для добавления минуты.
        """
        if self.second == 59:
            self.second = 0
            self.add_minute()
        else:
            self.second += 1


# Пример использования
if __name__ == "__main__":
    clock = Clock(23, 59, 58)
    clock.add_second()
    print(f"Time: {clock.hour:02}:{clock.minute:02}:{clock.second:02}")  # Time: 23:59:59
