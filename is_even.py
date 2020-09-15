# Исходная функция:
def is_even(number):
    ''' Returns True if **number** is even or False if it is odd. '''
    return number % 2


# Согласно docstring, функция возвращает True (1) в случае, если
# число четное. Иначе False (0).
# Простая проверка покажет, что функция работает неверно:
assert is_even(2) == 1, "ERROR! 2 is even"


# Если изменить функцию:
# def is_even(number):
#     return number % 2 == 0
# то она выдаст верные результаты
for i in [0, 1, 2, -222, -111]:
    assert is_even(i) == (i & 1 == 0), f'is_even({i}) = {is_even(i)} ERROR! {i} is {("even", "odd")[i & 1]}'
