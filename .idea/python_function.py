# built-in functions
def print_greeting():
    '''
    Print 'Hello!' text
    :return: None
    '''
    print('Hello!')

# call the function
print_greeting()

# receive the description of the function
help(print_greeting)

def print_greeting_with_name(name = 'Name'):
    '''
    :param name
    :return: None
    '''
    print('Hello ' + name + '!')
print_greeting_with_name('Jack')
help(print_greeting_with_name)
print_greeting_with_name()
x = print_greeting_with_name('Jane')
print(x)

def sum_of_two_numbers(a = 0, b = 0):
    '''
    :param a: The first addend
    :param b: The second addend
    :return: Sum of a and b
    '''
    return a + b
x = sum_of_two_numbers(45, 7)
x = sum_of_two_numbers()
print(x)
help(sum_of_two_numbers)

def is_hello_in_text(text):
    if 'hello' in text.lower():
        return True
    else:
        return False
print(is_hello_in_text('Hello everyone!'))

def is_hello_in_text(text):
    return 'hello' in text.lower()

print(is_hello_in_text('everyone!'))

def is_string_in_text(string, text):
    return string in text
print(is_string_in_text('he', 'The apple'))
print(is_string_in_text('hey', 'The apple'))

def greeting_depends_on_gender(name, gender):
    if gender == 'male':
        return gender
        print('Hello ' + name + '! You look great!')
    elif gender == 'female':
        print('Hello ' + name + '! You are so nice!')
        return gender
    else:
        print('Hello ' + name + '! I\'ve never seen the creature like you!')
        return gender


returned_value_1 = greeting_depends_on_gender('Jack', 'male')
returned_value_2 = greeting_depends_on_gender('Jane', 'female')
returned_value_3 = greeting_depends_on_gender('Ja', 'cmale')

print(returned_value_1)
print(returned_value_2)
print(returned_value_3)

# *args and **kwargs

# *args
def func_with_args(*args):
    print(args)
    print(type(args))
    print(len(args))

func_with_args(1, 2, 3)

def ten_percent_of_product_with_args(*args):
    product = 1
    for number in args:
        product = product * number
    return product * 0.1

print(ten_percent_of_product_with_args(10, 20, 2, 1, 4, 345))

def percent_of_product_with_args(percent, *args):
    product = 1
    for number in args:
        product = product * number
    return product / 100 * percent

print(percent_of_product_with_args(20, 10, 20, 2, 1, 4, 345))

# **kwargs
def func_with_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))

func_with_kwargs(first=1, second=2, third=3)

def hello_with_kwargs(**kwargs):
    if 'name' in kwargs:
        print('Hello! Nice to meet you, {}'.format(kwargs['name']))
    else:
        print('Hello! What is your name?')

hello_with_kwargs(gender='male', age=24, name='Jack')
hello_with_kwargs(gender='male', age=24)

def hello_with_greeting_and_kwargs(greeting, **kwargs):
    if 'name' in kwargs:
        print('{}! Nice to meet you, {}'.format(greeting, kwargs['name']))
    else:
        print('{}! What is your name?'.format(greeting))


hello_with_greeting_and_kwargs('Good morning', gender='male', age=24, name='Jack')
hello_with_greeting_and_kwargs('Good morning', gender='male', age=24)

def func_with_args_and_kwargs(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))

func_with_args_and_kwargs('one', 'two', drink='coffee', food='sandwich')

# Map, Filter and Lambda Expressions
# map()
def sum_of_two_numbers(x):
    return x + x

number_list = [1, 2, 3, 4, 5, 6, 7]
x = list(map(sum_of_two_numbers, number_list))
print(x)

def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has not "a"')
        return False

string_list = ['hi', 'was', 'name', 'he']
x = list(map(is_a_in_string, string_list))
print(x)

# filter()
def is_number_odd(number):
    return number % 2 == 1

number_list = [1, 2, 3, 4, 5, 6, 7]
# print(filter(is_number_odd, number_list))
x = list(filter(is_number_odd, number_list))
print(x)

for number in filter(is_number_odd, number_list):
    print(number)

def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has not "a"')
        return False

string_list = ['hi', 'was', 'name', 'he']
x = list(filter(is_a_in_string, string_list))
print(x)

# Lambda Expression применяем формулу/расчет ко всему списку
number_list = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda number: number ** 3, number_list)))
string_list = ['hi', 'was', 'name', 'he']
print(list(map(lambda string: string[-1], string_list)))
print(list(map(lambda string: string[::-1], string_list)))
print(list(filter(lambda number: number % 2 == 1, number_list)))
print(list(filter(lambda number: number % 2 == 0, number_list)))

# Higher order functions, which accept another functions as arguments
# финкции с другой функцией в качестве аргумента
def product(n, func):
    result = 1
    for number in range(1, n):
        result *= func(number)
    return result

def square(x):
    return x * x

def cube(x):
    return x * x * x

print(product(4, square))
print(product(4, cube))

# Using nested functions
# возвращение случайного элемента
from random import choice
def colorize(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color

    result = get_color() + ' ' + thing
    return result

print(colorize('apple'))

# Higher order functions, which return another function
# функция в функции
from random import choice
def make_color():
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color

    return get_color

first_color = make_color()
print(first_color())

# Inner functions can access outer function scope
from random import choice
def colorize1(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color + ' ' + thing

    return get_color

# print(colorize1('apple')())
colorized_dog = colorize1('dog')
print(colorized_dog())

# дополняем базовую функцию дополнительными вычислениями
def decorator_function(original_function):
    def wrap_function():
        print('Some code before the old code')
        original_function()
        print('Some code after the old code')
    return wrap_function


@decorator_function
def simple_function():
    print('Simple function code')

simple_function()

# дополнительные вычисления для любой функции переданной в качестве аргумента
def make_compliment(func):
    def wrapper(*args, **kwargs):
        print('Nice to meet you!')
        func(*args, **kwargs)
        print('You look great!')
    return wrapper

@make_compliment
def ask_name():
    print('What is your name?')

ask_name()

@make_compliment
def say_name(name):
    print('My name is ' + name)

say_name('Jack')

@make_compliment
def order(food, drink):
    print(f'Give me {food} and {drink}')

order(food='chips', drink='kola')

# wraps decorator
# добавляем к декорированной функции возможность увидеть ее имя и документацию
from functools import wraps

def print_function_data(function):
    """
    This is decorator function
    :param function:
    :return:
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are using {function.__name__}")
        print(f"Function documentation {function.__doc__}")
        return function(*args, **kwargs)
    return wrapper

@print_function_data
def squares_sum(a, b):
    """
    :param a: first number
    :param b: second number
    :return: sum of squares first and second numbers: (a * a + b * b)
    """
    return a * a + b * b

# print(squares_sum(2, 3))
print(squares_sum.__doc__)
print(squares_sum.__name__)
help(squares_sum)

# измерение скорости вычисления с помощью декоратора
from time import time
from functools import wraps

def speed_test(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time()
        print(f"Time of code execution {end_time - start_time}")
        return result
    return wrapper

@speed_test
def sum_with_list():
    return sum([number for number in range(10000000)])

print(sum_with_list())

# проверка аргументов с помощью декоратора
from functools import wraps

def prohibit_kwargs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('Keyword arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper

def prohibit_int_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for val in args:
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        for key, val in kwargs.items():
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper

@prohibit_int_arguments
def print_hello(name):
    print(f'Hello {name}!')

print_hello('Jack')
print_hello(3)

# проверка входящего значения с помощью декоратора
from functools import wraps

def check_if_first_arg_is(value):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                print(f'First argument has to be {value}')
            return func(*args, **kwargs)
        return wrapper
    return inner_dec

@check_if_first_arg_is('red')
def print_rainbow_colors(*colors):
    print(colors)

@check_if_first_arg_is(7)
def multiply_7(a, b):
    return a * b

print_rainbow_colors('orange', 'yellow', 'green', 'blue',
                     'indigo', 'violet')

print(multiply_7(7, 3))

