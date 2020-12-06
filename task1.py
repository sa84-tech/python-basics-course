class Date:
    date_str = ''

    def __init__(self, date_str):
        Date.set_date(date_str)

    @classmethod
    def set_date(cls, date_str):
        d = date_str.split('-')
        cls.day = int(d[0])
        cls.month = int(d[1])
        cls.year = int(d[2])

    @staticmethod
    def validate(day, month, year):
        print(Date)


date = Date('05-12-2020')
print(date.day, date.month, date.year)
