number = int(input('Введите число: '))
answer = 0
index1 = number

while index1 > 0:
    index2 = index1
    str1 = ''
    while index2 > 0:
        str1 += str(number)
        index2 -= 1
    answer += int(str1)
    index1 -= 1

print("Ответ: ", answer)
