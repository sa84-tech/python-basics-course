class Date:
    def __init__(self, date_str):
        Date.set_date(date_str)

    @classmethod
    def set_date(cls, date_str):
        d = date_str.split('-')
        try:
            day = int(d[0]) if Date.validate(day=int(d[0])) else 0
            month = int(d[1]) if Date.validate(month=int(d[1])) else 0
            year = int(d[2]) if Date.validate(year=int(d[2])) else 0
            if day and month and year:
                cls.day, cls.month, cls. year = [day, month, year]
            else:
                raise ValueError
        except (ValueError, IndexError):
            cls.day, cls.month, cls.year = [0, 0, 0]
            return print('Ошибка: некорректная дата.')

    @staticmethod
    def validate(day=0, month=0, year=0):
        if day:
            return False if day < 0 or day > 31 else True
        if month:
            return False if month < 0 or month > 12 else True
        if year:
            return False if year < 1900 or year > 2020 else True


while True:
    answer = (input('Введите дату в формате дд-мм-гггг (q для выхода): '))
    if answer == 'q':
        break
    date = Date(answer)
    print('День:', date.day, 'Месяц:', date.month, 'Год:', date.year)
