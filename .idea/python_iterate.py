# Iterables objects
number_list = [1, 2, 3, 4, 5]
for number in number_list:
    print(number)

for letter in 'my string':
    print(letter)

# Iterators
number_list = [1, 2, 3, 4, 5]
number_list_iterator = iter(number_list)
print(type(number_list_iterator))
string_iterator = iter('my string')
print(type(string_iterator))

print(number_list_iterator.__next__())
print(number_list_iterator.__next__())
print(next(number_list_iterator))
print(next(number_list_iterator))

print(string_iterator.__next__())
print(string_iterator.__next__())

## перебор итератора с помощью бесконечного цикла и try except
def my_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            print('Iteration is finished')
            break

my_for_loop('hello')
my_for_loop([1, 2, 3])

## класс итератор
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            number = self.current
            self.current += 1
            return number
        raise StopIteration

first_range = MyRange(20, 30)
for number in first_range:
    print(number)

# Generators are iterators
# Generators can be created with generator functions
# Generators can be created with generator expressions
def count_up_to(x):
    count = 1
    while count <= x:
        yield count
        count += 1


print(count_up_to(4))
counter = count_up_to(4)
print(counter.__next__())
print(counter.__next__())
print(next(counter))
print(next(counter))
print(list(count_up_to(7)))

# Infinite process
## изменеяем список на заданное количество элементов
def create_patterns(max_patterns_number, patterns):
    i = 0
    result_list = []
    while len(result_list) < max_patterns_number:
        if i >= len(patterns):
            i = 0
        result_list.append(patterns[i])
        i += 1
    return result_list

max_patterns_number = 12
patterns = ('First pattern', 'Second pattern', 'Third pattern',
            'Forth pattern')
print(create_patterns(max_patterns_number, patterns))

## перечислений элементов списка со сбрасыванием счетчика (бесконечный список)
def get_current_pattern():
    patterns = ('First pattern', 'Second pattern', 'Third pattern',
                'Forth pattern')
    i = 0
    while True:
        if i >= len(patterns):
            i = 0
        yield patterns[i]
        i += 1


current_pattern = get_current_pattern()
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())
print(current_pattern.__next__())

## засекаем время выполнения задачи
import time

list_start_time = time.time()
print(sum([number for number in range(1000000)]))
list_processing_time = time.time() - list_start_time

gen_start_time = time.time()
print(sum(number for number in range(100000000)))
gen_processing_time = time.time() - gen_start_time

print(f'Processing with list is {list_processing_time}')
print(f'Processing with generator is {gen_processing_time}')


