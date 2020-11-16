input_list = input('Введите несколько слов через пробел: ').split()

for i, el in enumerate(input_list):
    print(i + 1, el[0:10])
