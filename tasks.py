from random import random
func = lambda x: x + 15
print(func(10))

func2 = lambda x, y: x * y
print(func2(6, 8))


def func3(n):
    return lambda x: x * n
    
k = func3(5)
print(k(10))


lst_tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lst_tuples.sort(key=lambda x: x[1])
print(lst_tuples)


lst_dicts = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
             {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
             {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]