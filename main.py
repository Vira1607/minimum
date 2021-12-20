# Функция нахождения минимального числа
# без использования условного оператора, циклов и функции min.

def minimum(x, y):
  z = (x + y - abs(x - y)) / 2
  return z

number_first = int(input('Введите первое число: '))
number_twice = int(input('Введите второе число: '))

minimum(number_first, number_twice)

print('Наибольшее число:', z)
