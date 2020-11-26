# You need to install dependencies by running the command:
# pip install -r requirements.txt

from translator import get_translation

input_file_name = 'txt/text_4.txt'
output_file_name = 'txt/text_4_translated.txt'


def translate_file(file_name, log=False):
    """

    :param file_name: str - name and path of file to translate
    :param log: bool - if true, displays log of translating process
    :return: list
    """
    data_translation = []

    try:
        with open(file_name, encoding='utf-8') as f_obj:
            for i, line in enumerate(f_obj, 1):
                if log:
                    print(f'translating line {i}', end='... ')
                    line_translation = get_translation(line.rstrip('\n'))

                    if line_translation.get('warning'):
                        print('result:', line_translation.get('text') +
                              f' *Warning: {line_translation.get("warning")}')
                    elif line_translation.get('error'):
                        print('result:', line_translation.get('text') +
                              f' *Error: {line_translation.get("error")}')
                    else:
                        print('result:', line_translation.get('text'))
                else:
                    line_translation = get_translation(line.rstrip('\n'))

                data_translation.append(line_translation.get('text'))

        return data_translation
    except FileNotFoundError:
        return ['__ERROR__', f'File "{file_name}" Not Found']
    except IOError:
        return ['__ERROR__', 'I/O Error']
    except ValueError:
        return ['__ERROR__', 'Value Error']
    except TypeError:
        return ['__ERROR__', 'Type Error']


output_data = translate_file(input_file_name, log=True)

if output_data[0] != '__ERROR__':
    print('Результат перевода:', output_data)

    try:
        out_f = open(output_file_name, 'w', encoding='UTF-8')
        for output_line in output_data:
            out_f.write(f'{output_line}\n')

        print(f'Перевод текста успешно записан в файл {output_file_name}:')

    except IOError:
        print('I/O Error')
    finally:
        out_f.close()
else:
    print(output_data[1])
