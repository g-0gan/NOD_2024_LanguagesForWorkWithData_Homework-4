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

    def __add__(self, other):
        """
        Суммирует два объекта Clock, возвращая новый объект Clock.

        :param other: Другой объект Clock, который будет добавлен.
        :return: Новый объект Clock с суммарным временем.
        """
        hour = (self.hour + other.hour) % 24
        minute = (self.minute + other.minute) % 60
        second = (self.second + other.second) % 60
        return Clock(hour, minute, second)


# Пример использования
if __name__ == "__main__":
    clock1 = Clock(10, 30, 30)
    clock2 = Clock(3, 20, 40)
    new_clock = clock1 + clock2
    print(f"New time: {new_clock.hour:02}:{new_clock.minute:02}:{new_clock.second:02}")  # New time: 13:51:10
