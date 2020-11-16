months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
seasons = dict(January='Winter', February='Winter', March='Spring', April='Spring', May='Spring', June='Summer',
               July='Summer', August='Summer', September='Fall', October='Fall', November='Fall', December='Winter')
answer = 0
while answer > 12 or answer < 1:
    answer = input('Enter a number of month from 1 to 12: ')
    if answer.isdigit():
        answer = int(answer)
    else:
        answer = 0

month = months[int(answer) - 1]
print(f'Month: {month}, Season: {seasons.get(month)}')
