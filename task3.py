class IsNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def validate(inp):
        try:
            float(inp)
        except ValueError:
            return False
        return True


final_list = []
proceed = True

while proceed:
    answer = input('Введите число (stop для выхода): ')
    if answer == 'stop':
        break
    try:
        if IsNumberError.validate(answer):
            final_list.append(float(answer))
        else:
            raise IsNumberError('Только числа.')
    except IsNumberError as err:
        print(err)


print('Итоговый список:\n', final_list)
