def organize_personal_data(first_name, last_name, birth_year, residence_city, email, phone):
    """
    Возвращает строку с данными пользователя переданными в качестве аргументов
    :param first_name: str
    :param last_name: str
    :param birth_year: str
    :param residence_city: str
    :param email: str
    :param phone: str
    :return: str
    """

    return f'Данные пользователя {first_name} {last_name}\n    Год рождения: {birth_year}\n' \
           f'    Город проживания: {residence_city}\n    Электроная почта: {email}\n    Телефон: {phone}\n'


print(organize_personal_data(
    first_name=input('Введите данные пользователя.\nИмя: '),
    last_name=input('Фамилия: '),
    birth_year=input('Год рождения: '),
    residence_city=input('Город проживания: '),
    email=input('Электронная почта: '),
    phone=input('Телефон: '),
))
