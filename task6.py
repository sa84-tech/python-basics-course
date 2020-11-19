def int_func(word):
    """
    Принимает слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой
    :param word: str
    :return: str
    """
    for letter in word:
        l_code = ord(letter)
        if l_code < 97 or l_code > 122:
            return ''
    return f'{chr(ord(word[0]) - 32)}{word[1:]} '


string = 'Dfdf df343df dfвdfd ываhыва htrt rtrt tttrr sdffefe'

print(''.join(map(int_func, string.split())))
