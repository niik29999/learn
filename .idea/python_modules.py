# импорт из встроенных модулей
import random
x = random.randint(1, 10)
print(x)

from random import randint
x = randint(1, 10)
print(x)

from random import shuffle
my_list = [1,2,3]
shuffle(my_list)
print(my_list)

from random import shuffle as shuffle_my_list
my_list = [1,2,3]
shuffle_my_list(my_list)
print(my_list)

# импортируем функции из других скриптов
from python_function import print_greeting
print_greeting()

# импорт из внешних модулей
## C:\Users\niik2\AppData\Local\Programs\Python\Python37\python.exe -m pip install termcolor
## C:\Users\niik\anaconda3\python.exe -m pip install fdb
# pip3 install numpy
import termcolor

print(termcolor.colored('Hello termcolor', 'green', 'on_yellow'))
# help(termcolor)


