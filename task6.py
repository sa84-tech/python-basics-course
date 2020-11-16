goods = []
repeat = 'д'
count = 0
name_arr = []
price_arr = []
quantity_arr = []
unit_arr = []

while repeat == 'д':
    count += 1
    goods_name = input('Добавление нового товара.\nВведите наименование товара: ')
    goods_price = input('Укажите цену: ')
    goods_quantity = input('Укажите количество: ')
    goods_unit = input('Укажите единицы измерения: ')

    goods.append(
        (count, dict(название=goods_name, цена=goods_price, количество=goods_quantity, ед=goods_unit))
    )

    repeat = input('Повторить? (д/н)')

print('Товары\n', goods)

for el in goods:
    name_arr.append(el[1].get("название"))
    price_arr.append(el[1].get("цена"))
    quantity_arr.append(el[1].get("количество"))
    unit_arr.append(el[1].get("ед"))

analitics_dict = dict(название=name_arr, цена=price_arr, количество=quantity_arr, ед=unit_arr)

print('Аналитика\n', analitics_dict)