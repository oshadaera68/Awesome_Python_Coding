# [1,2,3,4,5,6] -> 1,2,3,4,5,6
# def my_sum(*args):
#     result = 0
#     for param in args:
#         result += param
#     return result
#
#
# print(my_sum(10, 20, 30, 40, 50, 60))

# **{'a': 1, 'b': 2, 'c': 3} -> myfunction(a=1, b=2, c=3)

def myprint(name, age, job):
    print(f'{name} is {age} years old and works as a {job}.')


dict1 = {'name': 'Mike', 'age': 30, 'job': 'Programmer'}
dict2 = {'height': 185, 'weight': 80}

combined_dic = {**dict1, **dict2}
print(combined_dic)


def my_function(**kwargs):
    print('The following parameters were passed:')
    for k, v in kwargs.items():
        print(f'Parameter Name:{k}, Parameter Value:{v}')


my_function(name='John', test='Hello', other='World')
