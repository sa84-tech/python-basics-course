file_name = 'txt/text_6.txt'
subject_dict = {}

try:
    with open(file_name) as f_obj:

        for line in f_obj:
            subject_hours_sum = 0

            for i, l in enumerate(line.split()):
                if i == 0:
                    subject_name = l[:-1]
                else:
                    n = ''.join(s for s in l if s.isdigit())
                    if n:
                        subject_hours_sum += int(n)
            subject_dict.update({subject_name: int(subject_hours_sum)})

except IOError:
    print('I/O Error')

print(subject_dict)
