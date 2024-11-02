def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()  # вызов сработал
# print_params(a, b)  вышла ошибка

values_list = [1, True, "Kate"]
values_dict = {"a": 54.32, "b": 15, "c": "Dima"}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, "Строка"]
print_params(*values_list_2, 42) 
