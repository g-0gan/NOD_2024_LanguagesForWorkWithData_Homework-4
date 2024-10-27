class Counter:
    def __init__(self):
        """
        Инициализирует объект счётчика со значением по умолчанию 0.
        """
        self.value = 0

    def increment(self):
        """
        Увеличивает значение счётчика на 1.
        """
        self.value += 1

    def decrement(self):
        """
        Уменьшает значение счётчика на 1, если текущее значение больше 0.
        """
        if self.value > 0:
            self.value -= 1

    def get_counter(self):
        """
        Возвращает текущее значение счётчика.

        :return: Текущее значение счётчика.
        """
        return self.value


# Пример использования
if __name__ == "__main__":
    counter = Counter()
    counter.increment()
    counter.increment()
    counter.decrement()
    print("Counter value:", counter.get_counter())  # Counter value: 1
