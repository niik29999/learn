def get_rainbow_color(color_number):
    '''
    :param color_number: Color number must be integer type
    and must be in range of integer from 1 to 7
    :return:
    '''

    color_number_list = [1, 2, 3, 4, 5, 6, 7]
    if type(color_number) is not int:
        raise TypeError('Color number must be integer type')

    if color_number not in color_number_list:
        raise ValueError('Color number must be in range of integer '
                         'from 1 to 7')

    if color_number == 1:
        return 'red'
    elif color_number == 2:
        return 'orange'
    elif color_number == 3:
        return 'yellow'
    elif color_number == 4:
        return 'green'
    elif color_number == 5:
        return 'blue'
    elif color_number == 6:
        return 'indigo'
    elif color_number == 7:
        return 'violet'

## передаем тип int ошибки нет
color = get_rainbow_color(1)
print(color)
## передаем не int, возвращается ошибка типа TypeError
color = get_rainbow_color(1.0)
print(color)
## передаем значение не в диапазоне, возвращается ошибка типа ValueError
color = get_rainbow_color(8)
print(color)

# try except
## пыатаемся применить функцию len к int что приводит к TypeError
try:
    # print(my_variable)
    print(len(23))
except NameError:
    print('NameError has happen')
except TypeError:
    print('TypeError has happen')
print('Code after error')

## если передан ключ которого нет в словаре, то функция не падает с ошибкой KeyError, а возвращает None
user_dictionary = {'first_name': 'Jack', 'last_name': 'White', 'age': 24}
def get_dictionary_values(dictionary, key):
    '''
    If dictionary hasn't specified key, the function returns None
    :param dictionary:
    :param key:
    :return:
    '''
    try:
        return dictionary[key]
    except KeyError:
        return None

print(get_dictionary_values(user_dictionary, 'age'))
print(get_dictionary_values(user_dictionary, 'a'))

# If we have an error - except block fires and else block doesn't fire
# If we haven't an error - else block fires and except block doesn't fire
# Finally block fires anyway
while True:
    try:
        number = int(input('Enter some number'))
        print(number / 2)
    except:
        print('You have to enter a number!')
    else:
        print('Good job! This is a number!')
        break
    finally:
        print('Finally block')

print('Code after error handling')


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        print('You can\'t divide by zero!')
        print(e)
    except TypeError as e:
        print('x and y must be numbers')
        print(e)
    else:
        print('x was divided by y')
    finally:
        print('finally block')

#print(divide(4, 0))
print(divide(4, 'w'))

