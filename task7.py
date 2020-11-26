from statistics import mean
import json

input_file_name = 'txt/text_7.txt'
output_file_name = 'txt/text_77.json'
companies = {}

try:
    with open(input_file_name, encoding='utf-8') as read_f:
        for line in read_f:
            cur_cmp = line.split()
            companies.update({cur_cmp[0]: float(cur_cmp[2]) - float(cur_cmp[3])})

    average_profit = dict(average_profit=mean(s for s in companies.values() if s > 0))

    result_list = [companies, average_profit]
    print(result_list)

    with open(output_file_name, 'w', encoding='utf-8') as write_f:
        print(json.dumps(result_list, ensure_ascii=False), file=write_f)

except IOError:
    print('I/O Error')
except ValueError:
    print('Value Error')


