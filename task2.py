time = int(input('Пользователь, введи время в секундах: '))

hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60

if hours < 10:
    hours = f'0{hours}'
if minutes < 10:
    minutes = f'0{minutes}'
if seconds < 10:
    seconds = f'0{seconds}'

print(f'{hours}:{minutes}:{seconds}')
