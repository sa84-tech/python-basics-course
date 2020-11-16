input_list = input('Введите элементы списка через пробел: ').split()
print('исходный список: ', input_list)

for el in range(0, len(input_list) - 1, 2):
    if input_list[el + 1]:
        input_list[el], input_list[el + 1] = input_list[el + 1], input_list[el]

print('   новый список: ', input_list)
