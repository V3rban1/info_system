text = input('Введите ваш запрос: ')

if text.isnumeric():
    print('Вы ввели число:', text)
else:
    print('Ваш запрос содердит только строку.')