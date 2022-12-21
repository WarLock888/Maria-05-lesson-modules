def bank_account():
    acount = 0
    purchases =[]

    while True:
        print(f'На Вашем счете {acount}')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            refill = int(input('Какую сумму хотите внести?: '))
            acount += refill
        elif choice == '2':
            expenses = int(input('Какую сумму потратим?: '))
            if expenses > acount:
              print('Не достаточно средств')
            else:
              item = input('Что покупаем?: ')
              good=[item,expenses]
              purchases.append(good)
              acount -= expenses
        elif choice == '3':
            print()
            print('Ваши покупки:', purchases)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
        print()

if __name__ == '__main__':
    bank_account()