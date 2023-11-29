def check_answer(question, correct_answer):
    answer = input(question)
    while answer != correct_answer:
        print("Не верно")
        answer = input(question)
    print("Все верно")

# Использование функции для проверки года рождения
check_answer('Введите год рождения А.С.Пушкина: ', '1799')

# Использование функции для проверки дня рождения
check_answer('В какой день июня родился Пушкин? ', '6')
