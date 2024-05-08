from deprecated import deprecated


# 1.4.3
@deprecated(reason="Calculate will be removed in future versions, use add, sub, etc. instead.", version="1.4.3")
def calculate(number1, number2, operator):
    return eval(f'{number1} {operator} {number2}')


def add(number1, number2):
    return number1 + number2


def sub(number1, number2):
    return number1 - number2


print(calculate(10, 20, '+'))
