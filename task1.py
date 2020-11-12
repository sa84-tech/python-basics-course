repeat = 'д'
while repeat == 'д':
    name = input('Как тебя зовут? ')
    age = input(f'Привет, {name}, сколько тебе лет?')
    print(f'{name}, я только что узнал твой возраст - {age}.')
    repeat = input('Еще раз? (д/н) ')
