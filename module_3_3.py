# Распаковка позиционных параметров
def print_params(a=1, b='строка', c=True):
    print(a,b,c)
print_params()
print_params(2,'-----')
print_params(b=25)
print_params(c=[1,2,3])
value_list = [10.2,'строка', False]
value_dict = {'a':8, 'b':'Tom', 'c':False}
print_params(*value_list)
print_params(**value_dict)
# Распаковка + отдельные параметры
value_list2 = [5,'key']
print_params(*value_list2, 42) # здесь передается с:42
