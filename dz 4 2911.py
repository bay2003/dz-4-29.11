def simple_separator():

    separator = '*' * 10
    return separator

print(simple_separator())

def long_separator(count):

    return '*' * count

print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True

def separator(simbol, count):

    return simbol * count

print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True

def hello_world():

    print('**********')
    print('\nHello World!\n')
    print('##########')

hello_world()

def hello_who(who='World'):

    print('**********')
    print(f'\nHello {who}!\n')
    print('##########')


name = input('Назовите Ваше имя: ')
hello_who(name)

def hello_who(who):

    print('**********')
    print(f'\nHello {who}!\n')
    print('##########')

# Запрос имени пользователя и вызов функции
name = input('Назовите Ваше имя: ')
hello_who(name)

def pow_many(power, *args):

    total_sum = sum(args)
    return total_sum ** power

# Тестирование функции
print(pow_many(1, 1, 2) == 3)  # True
print(pow_many(1, 2, 3) == 5)  # True
print(pow_many(2, 1, 1) == 4)  # True
print(pow_many(3, 2) == 8)  # True
print(pow_many(2, 1, 2, 3, 4) == 100)  # True

def print_key_val(**kwargs):

    for key, value in kwargs.items():
        print(f'{key} --> {value}')

# Примеры использования функции
print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)

def my_filter(iterable, function):

   
    filtered = []
    for item in iterable:
        if function(item):
            filtered.append(item)
    return filtered

# Примеры использования функции
print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True








