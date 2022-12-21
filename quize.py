
def games():
    import random
    game = 'YES'
    AUTHORS = {
        'Пушкин': '06.06.1799',
        'Толстой': '09.09.1828',
        'Лермонтов': '15.10.1814',
        'Гоголь': '20.03.1807',
        'Достоевский': '11.11.1821',
        'Дюма': '24.07.1802',
        'Шекспир': '23.04.1564',
        'Бунин': '22.10.1870',
        'Некрасов': '10.12.1821',
        'Тютчев': '23.11.1803',
    }

    def pushkin_day(questions):
        correct = 0
        mistakes = 0
        for k in questions:
            answer_k = input(f'Когда родился {k}? ')
            if AUTHORS[k] == answer_k:
                correct += 1
            else:
                mistakes += 1
        print(f'Верных ответов {correct}, {correct * 100 / (correct + mistakes)} % ')
        print(f'Неверных ответов {mistakes}, {mistakes * 100 / (correct + mistakes)} % ')
        return None

    while game == 'YES':
        correct = 0
        mistakes = 0
        questions = random.sample(list(AUTHORS), 5)
        pushkin_day(questions)
        game = input('Играем еще (yes/no)?: ').upper()

if __name__ == '__main__':
    games()