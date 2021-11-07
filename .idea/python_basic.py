import psycopg2

# присвоение переменных
x = y = z = 12
print(x, y, z)

x, y, z = 12, 13, 14
print(x, y, z)

# цикл в заданном диапазон
for x in range(10):
    print(x)ште()

# числовой диапазон в лист
x = list(range(5))
print(x)
x = list(range(1,15,2))
print(x)

# перемешать диапазон
from random import shuffle
shuffle(x)
print(x)

# случайное число
from random import randint
print(randint(2,20))

# min, max
print(min(1, 3, 56, 4))
print(max(1, 3, 56, 4))

# форматирование длинной строки
whole_sentence = 'Hello Jack' + " " \
                 + 'White!'
print(whole_sentence)

# задержка выполнения
import time
time.sleep(60) # задержка 60 секунд

# текущая дата и время
import datetime
day = datetime.datetime.today()
day2 = datetime.datetime.now()
print(day)
print(day2)
print(day2 + datetime.timedelta(10))
print(day.year)

# поиск(find, like) в строке
print('a' in 'apple')
print('s' in 'apple')

# Escaping \
some_string = 'I\'m a programmer'
print(some_string)
another_string = "I want to learn \"Python\""
print(another_string)

# перенос
string_with_new_lines = "Hello! \n          \rMy name is YouRa"
print(string_with_new_lines)

# отступ
some_text = "\tHello! \n\tI'm very glad to see you!"
print(some_text)

# Triple quotes
string_with_triple_quotes = """This is ' 
text with 
"triple 
quotes" """
another_string_with_triple_quotes = '''This is ' text with "triple quotes" '''
print(string_with_triple_quotes)
print(another_string_with_triple_quotes)

# Len
greeting = 'Hello Python!'
greeting_length = len(greeting)
print(len(greeting))

# Indexing
print(greeting[1])
print(greeting[-1])

# Slicing
print(greeting[2:5])
print(greeting[-5:-2])
print(greeting[2:])
print(greeting[:5])
print(greeting[:])
print(greeting[::2])
print(greeting[::1])
print(greeting[1::3])
print(greeting[1:9:3])
print(greeting[::-1])

# Multiplication
yummy = 'Yum '
print(yummy * 3)
print(yummy.upper())
print(yummy.lower())

# split
long_string = 'This is the long string'
print(long_string.split(' '))

# собираем строки для вывода
print(1 + 1)
print('1' + '1')
age = 23
print('Jack is ' + str(age) + ' years old.')
print('Jack is ' + str(23) + ' years old.')

name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)
name_and_age = 'My name is {0}. I\'m {1} years old.'.format('Jack', 23)
print(name_and_age)
name_and_age = 'My name is {}. I\'m {} years old.'.format(23, 'Jack')
print(name_and_age)
week_days = 'There are 7 days in a week: {5}, {0}, {3}, {1}, {2}, {4}, {6}.'\
    .format('Monday', 'Wednesday', 'Thursday','Tuesday', 'Friday', 'Sunday',
            'Saturday')
print(week_days)
week_days = 'There are 7 days in a week: {su}, {mo}, {tu}, {we}, {th},' \
            ' {fr}, {sa}.' \
    .format(mo = 'Monday', we = 'Wednesday', th = 'Thursday',
            tu = 'Tuesday', fr = 'Friday', su = 'Sunday',
            sa = 'Saturday')
print(week_days)
week_days = 'There are 7 days in a week: {su}, {su}, {su}, {su}, {su},' \
            ' {su}, {su}.' \
    .format(mo = 'Monday', we = 'Wednesday', th = 'Thursday',
            tu = 'Tuesday', fr = 'Friday', su = 'Sunday',
            sa = 'Saturday')
print(week_days)

float_result = 1000 / 7
print(float_result)
print('The result of division is {0:10.3f}'.format(float_result))
print('''
 {0:10.2f} {1:10.2f} {2:10.2f}
 {3:10.2f} {4:10.2f} {5:10.2f}
 {6:10.2f} {7:10.2f} {8:10.2f}
'''.format(1.45778, 345.232352, 34.2344, 1234.23,
           1.45778, 345.232352, 34.2344, 1234.23,
           456.43234))

name = 'Jack'
age = 23
name_and_age = f'My name is {name}. I\'m {age} years old.'
print(name_and_age)
print('My name is %s. %s %d years old' % (name, "I'm", age))

# Input
x = input('Input something')

# Output
print('Output something' + x)
print(1, 2, 3, sep=':', end='\n')
print(1, 2, 3, sep=',', end=' ')
print(1, 2, 3, sep=';', end='')

# if __name__ == '__main__':
# если интерпретатор запускает некоторый модуль (исходный файл) как основную программу, он
# присваивает специальной переменной __name__ значение "__main__".
# Если этот файл импортируется из другого модуля, переменной __name__ будет
# присвоено имя этого модуля

# области действия переменной
## Local Scope переназначение переменной в функции не влияет на ее внешнее значение
pi = 'outer pi variable'
def print_pi():
    pi = 'inner pi variable'
    print(pi)

print_pi()
print(pi)

## Enclosed Scope
pi = 'global pi variable'
def outer():
    pi = 'outer pi variable'
    def inner():
        # pi = 'inner pi variable'
        global pi
        print(pi)
    inner()
    print(pi)

outer()
print(pi)

## Built-in Scope встроенные переменные
from math import pi
print(pi)

# List
some_list = [12, 35.334, 'hello']
print(some_list)
print(len(some_list))
print(some_list[1])
another_list = some_list[:2]
print(another_list)
some_list[2] = 'hi'
print(some_list)
new_list = some_list + another_list
print(new_list)

# Adding items
new_list.append('new item')
new_list.insert(0, 'start')
print(new_list)

# Removing items
deleted_item = []
## удаление по номеру
deleted_item.append(new_list.pop(-1))
deleted_item.append(new_list.pop(0))
## удаление конретного значения
deleted_item.append(new_list.remove(12))

print(new_list)
print(deleted_item)

# сортировка List
number_list = [45, 12, 3, -455, 22]
letter_list = ['s', 'w', 't', 'a']

## сначало надо отсортировать сам массив
number_list.sort()
letter_list.sort()
x = number_list
new_list = letter_list

print(x)
print(new_list)

# обратный порядок List
number_list.reverse()
letter_list.reverse()

print(number_list)
print(letter_list)

# Dictionary
car_prices = {'opel': 5000, 'toyota': 7000, 'bmw': 10000 }
print(car_prices)
print(car_prices['toyota'])
car_prices['mazda'] = 4000
print(car_prices)
car_prices['opel'] = 2000
print(car_prices)
del car_prices['toyota']
print(car_prices)
car_prices.clear()
print(car_prices)

person = {
    'first name': 'Jack',
    'last name': 'Brown',
    'age': 43,
    'hobbies': ['football', 'singing', 'photo'],
    'children': {'son': 'Michael', 'daugter': 'Pamela'}
}

print(person['age'])
print(person['hobbies'])
hobbies = person['hobbies']
print(hobbies[2])

# tuple
tuple_1 = 1, 2, 3
new_tuple = (tuple_1[0], 3, tuple_1[-1])
print(new_tuple)
print(tuple_1[1])
print(type(tuple_1))

## присвоение переменных из tuple
person_tuple = ('John', 'Smith', 1986)
first_name, last_name, year_of_birth = person_tuple
print(first_name, last_name, year_of_birth)

## считаем количество значений в tuple
t1 = (1, 2, 5, 1, 7, 9)
print(t1.count(1))
greetings_tuple = ('hello', 'hi', 'hey', 'hi')
print(greetings_tuple.count('hola'))

## возвращаем индекс значения, если оно уникально
print(t1.index(5))
print(t1.index(1))
print(greetings_tuple.index('hi'))

# Sets
rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue',
                  'indigo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 43, 56, 3, 3, 3, 3]
text_tuple = ('sfds', 'aafg', 'afadsf', 'hi', 'hi', 'hi')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(777)
set_from_tuple.add('hello')
set_from_list.add(777)
set_from_tuple.add('hello')

x = set_from_list.pop()
set_from_list.remove(3)
set_from_list.discard(43)
set_from_list.discard(3)
set_from_list.clear()

print(set_from_list)
print(set_from_tuple)
print(x)

# boolen
print(1 < 2)
print(type(True))
print(type(False))

## Comparison operators
print(1 == 1)
print(1 == 2)
print('Hello' == 'Hello')
print('Hello' == 'hello')

print(1 != 1)
print(1 != 2)
print('Hello' != 'Hello')
print('Hello' != 'hello')

print(1 > 2)
print(1 < 2)
print(2 >= 2)
print(3 >= 2)
print(2 <= 2)
print(3 <= 2)

print(ord('a'))
print(ord('b'))
print('a' > 'b')
print('hi' > 'hello')
print(ord('i'))
print(ord('e'))

x = 10
y = 23
print(x > y)
print(x < y)
print(x == y)
print(x != y)

# logical_operators and, or, not
x = 1
y = 2

print(x > 1 and y > 1)
print(x > 1 or y > 1)
print(not x > 1)
print(not y > 1)
print(True and True)
print(True or True)
print(not True)
print(False and False)
print(False or False)
print(not False)
print(True and False)
print(True or False)

# conditional_operators
day_time = 'midnight'
if day_time == 'morning':
    print('Monster wakes up')
elif day_time == 'afternoon':
    print('Monster is walking')
elif day_time == 'evening':
    print('Monster is eating')
elif day_time == 'night':
    print('Monster is sleeping')
else:
    print('Monster is doing something')

x = 41
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')
print('Some text')

# for_loop
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    print(str(number) + ' Hola!')

for number in number_list:
    if number % 2 == 0:
        print(number)
    else:
        print('Hey!')

list_numbers_sum = 0
for number in number_list:
    list_numbers_sum = list_numbers_sum + number
print(list_numbers_sum)

greeting = 'Hello Python!'
for letter in greeting:
    print(letter)

greeting = 'Hello Python!'
for letter in greeting:
    if letter != 'o':
        print(letter)

print(sum([number for number in range(10)]))

tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for item in tuple_list:
    print(item)
for letter_1, letter_2 in tuple_list:
    print(letter_1, letter_2)
for letter_1, letter_2 in tuple_list:
    print(letter_1)

tuple_list_1 = [('a', 'b', 1), ('c', 'd', 4), ('e', 'f', 5)]
for letter_1, letter_2, number in tuple_list_1:
    print(letter_1, letter_2, number)

print(sum(number for number in range(10)))

dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# key-value pairs in tuples
for item in dictionary.items():
    print(item)

# keys
for item in dictionary:
    print(item)
for item in dictionary.keys():
    print(item)
for key, value in dictionary.items():
    print(key)

# values
for item in dictionary.values():
    print(item)
for key, value in dictionary.items():
    print(value)

for _ in range(5):
    print('Hello!')

for i in range(5):
    print('Hello!')
    print(i)

# while_loop
x = 5
while x >= 1:
    print(x)
    x -= 1          # x = x - 1

while x < 10:
    print(x)
    x += 1          # x = x + 1

while x < 10:
    print(x)
    x += 2
print('Next code')

x = 0
while x < 10:
    print(str(x) + ' x is less than 10')
    x += 1
else:
    print(str(x) + ' x now is not less than 10')

for x in range(10):
    print(str(x) + ' x is less than 10')
else:
    x += 1
    print(str(x) + ' x now is not less than 10')

# break, continue, pass
my_list = [1, 2, 3]

for item in my_list:
    pass
print('Another code')

for item in my_list:
    if item == 2:
        break
    print(item)
print('Another code')

for item in my_list:
    if item == 2:
        continue
    print(item)
print('Another code')

# useful_operators
## значение и его индекс
my_string = 'adfagasg'
for index, letter in enumerate(my_string):
    print(letter + ' is at index ' + str(index))

## проверка вхождения в строку
print('a' in 'Jack')
print('x' in 'Jack')
print(str(1) in 'Jack')
print('1' in 'Jack')

letter_list = ['a', 'b', 'c', True]
print('a' in letter_list)
print(True in letter_list)

dict_1 = {1: 'a', 2: 'b', 3: 'c'}
print(1 in dict_1)
print(1 in dict_1.keys())
print(4 in dict_1.keys())
print('c' in dict_1.values())
print('z' in dict_1.values())

my_list = [1, 3, 56, 4]
print(min(my_list))
print(max('Hello'))
for letter in 'Hello':
    print(ord(letter))

from random import shuffle
my_list = [1, 3, 56, 4]
shuffle(my_list)
print(my_list)

# List Comprehension
greeting = 'hello!'
letter_list = []
for letter in greeting:
    letter_list.append(letter)
print(letter_list)

letter_list = [letter for letter in greeting]
print(letter_list)
number_list = [number for number in '0123456789']
print(number_list)
number_list_1 = [num for num in range(0, 10)]
print(number_list_1)
number_list_2 = [num ** 2 for num in range(0, 10)]
print(number_list_2)
number_list_3 = [- ((num - 3) / 2) ** 2 for num in range(0, 10)]
print(number_list_3)
number_list = [6, 43, -2, 11, -55, -12, 3, 345, 0]
new_list = [number ** 3 / 2 for number in number_list if number > 0]
print(new_list)
new_list_1 = ['+' if number > 0 else '-' if number < 0
              else 'zero' for number in number_list]
print(new_list_1)

# Dictionary Comprehension
number_dict = {'first': 1, 'second': 2, 'third': 3}
new_dict = {key: value ** 3 for key, value in number_dict.items()}
print(new_dict)

number_list = [6, 43, 0, -2, 11, -55, -12, 3, 345]
number_dict = {number: number ** 2 for number in number_list}
print(number_dict)
number_dict = {number: 'positive' if number > 0
else 'negative' if number < 0 else 'zero' for number in number_list}
print(number_dict)

# Set Comprehension
number_list = [6, 43, 0, -2, 11, -55, -12, 3, 345]
number_set = {number ** 2 for number in number_list}
print(number_set)
number_set = {number ** 2 for number in range(3, 11)}
print(number_set)
letter_set = {letter.upper() for letter in 'hello'}
print(letter_set)

