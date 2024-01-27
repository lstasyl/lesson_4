my_list = [1]

if len(my_list) > 1:
    index = len(my_list) - 1
    multiplicand = my_list[index]
    num_1 = sum(my_list[0:index:2])
    result = num_1 * multiplicand
else:
    result = my_list[0] ** 2

print(result)
