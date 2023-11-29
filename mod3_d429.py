def top_up_balance(user_balances, user):
    amount = float(input("Введите сумму для пополнения: "))
    user_balances[user] += amount

def make_purchase(user_balances, user, purchase_history, products):
    print("Доступные товары и их цены:")
    for product, price in products.items():
        print(f"{product}: {price} руб.")

    chosen_product = input("Введите название товара для покупки: ")
    if chosen_product in products:
        price = products[chosen_product]
        if user_balances[user] >= price:
            user_balances[user] -= price
            purchase_history.append((user, chosen_product, price))
            print(f"Вы купили {chosen_product} за {price} руб.")
        else:
            print("Недостаточно средств на счету.")
    else:
        print("Товар не найден.")

def show_purchase_history(purchase_history, user):
    for usr, item, amount in purchase_history:
        if usr == user:
            print(f"{item}: {amount} руб.")

def main_menu():
    user_balances = {'max': 15, 'mara': 20, 'jony': 30, 'miha': 15}
    purchase_history = []
    products = {'serv': 15, "baks": 30, "mini": 10}

    user = input("Как Вас зовут? ")
    if user in user_balances:
        while True:
            print(f'Текущий баланс: {user_balances[user]} руб.')
            print('1. Пополнение счета')
            print('2. Покупка')
            print('3. История покупок')
            print('4. Выход')

            choice = input('Выберите пункт меню: ')
            if choice == '1':
                top_up_balance(user_balances, user)
            elif choice == '2':
                make_purchase(user_balances, user, purchase_history, products)
            elif choice == '3':
                show_purchase_history(purchase_history, user)
            elif choice == '4':
                break
            else:
                print('Неверный пункт меню')
    else:
        print("Имя пользователя не найдено.")

main_menu()
