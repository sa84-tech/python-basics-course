from functools import reduce

new_list = [el for el in range(100, 1001) if el % 2 == 0]

result = reduce((lambda mul, cur: mul * cur), new_list)

print(new_list)
print(result)
