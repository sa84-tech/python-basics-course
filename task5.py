rating = [7, 5, 3, 3, 2]
print('Текущий рейтинг:', rating)

while True:
    answer = input('Укажите вашу оценку от 1 до 9 (q для выхода) ')
    if answer == 'q':
        break
    if (not answer.isdigit()) or int(answer) < 1 or int(answer) > 9:
        continue

    if int(answer) <= int(rating[-1]):
        rating.append(answer)
    else:
        for i, el in enumerate(rating):
            if int(answer) > int(el):
                rating.insert(i, answer)
                break
    print('Обновленный рейтинг:', rating)
