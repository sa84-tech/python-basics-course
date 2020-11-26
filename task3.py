def print_salary_report(file_name):
    salary_report = []
    lucky_list = []
    salary_sum = 0

    try:
        with open(file_name, encoding='utf-8') as f_obj:
            for line in f_obj:
                salary_report.append(line.split())

        for el in salary_report:
            cur_salary = float(el[1])
            salary_sum += cur_salary
            if cur_salary < 20000:
                lucky_list.append(el[0])

    except IOError:
        print('I/O Error')
        return
    except ValueError:
        print('Value Error')
        return

    print(f'Средняя зарплата всех сотрудников: {round(salary_sum / len(salary_report), 2)} руб.')
    print('Список сотрудников с зарплатой ниже 20000 руб.:\n', lucky_list)


print_salary_report('txt/text_3.txt')
