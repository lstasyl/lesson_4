def myfunc(n):
    return abs(n - 0)

this_list = [0, 1, 2, 6, 0, 0, 5, 4, 65, 0, 756, 0]
this_list.sort(key=myfunc)
index = this_list.count(0)              #рахухе кількість "0"
list_0 = this_list[:index]
del this_list[:index]
result = this_list + list_0

print(result)