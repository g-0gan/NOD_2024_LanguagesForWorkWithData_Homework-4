# Таблица перевода оценок
grade_conversion = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'F': 1,
    5: 'A',
    4: 'B',
    3: 'C',
    2: 'D',
    1: 'F'
}


def convert_grade(input_grade):
    """
    Переводит оценку из буквенного в числовое значение и наоборот.

    :param input_grade: Оценка в виде строки (буква) или числа.
    :return: Числовое значение оценки для буквенных оценок или буквенная оценка для числовых значений.
    :raises ValueError: Если оценка не является допустимым значением.
    """
    if input_grade in grade_conversion:
        return grade_conversion[input_grade]
    else:
        raise ValueError("Недопустимое значение оценки")


if __name__ == "__main__":
    print("Введите оценку для перевода. Пустая строка завершит программу.")
    while True:
        user_input = input("Введите оценку (букву или число): ").strip()
        if not user_input:
            print("Программа завершена.")
            break

        try:
            # Попытка сначала интерпретировать ввод как число, затем как строку
            try:
                grade = int(user_input)
            except ValueError:
                grade = user_input.upper()

            converted_grade = convert_grade(grade)
            print(f"Преобразованная оценка: {converted_grade}")
        except ValueError as e:
            print(e)
