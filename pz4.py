input_data = input('Введите ваш запрос: ')

if not input_data:
    print('Пустой ввод.')
elif input_data.startswith('https://'):
    print('Ваш запрос похож на веб-ресурс.')
elif input_data.endswith('.txt'):
    print('Ваш запрос похож на файл формата TXT.')
elif input_data.isnumeric():
    print('Вы ввели число:', input_data)
else:
    print('Ваш запрос содержит только строку.')