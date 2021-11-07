# прочитать текстовый файл
lorem_ipsum_text = open('E:\work\Python\python_course\sample.txt', 'r')
for line in lorem_ipsum_text:
    print(line,end='')
lorem_ipsum_text.close()

with open('E:\work\Python\python_course\sample.txt', 'r') as lorem_ipsum_text:
    line = lorem_ipsum_text.readline()
    while line:
        print(line, end='')
        line = lorem_ipsum_text.readline()

## читаем с условием
lorem_ipsum_text = open('E:\work\Python\python_course\sample.txt', 'r')
for line in lorem_ipsum_text:
    if 'mary' in line.lower():
        print(line,end='')
lorem_ipsum_text.close()

with open('E:\work\Python\python_course\sample.txt', 'r') as lorem_ipsum_text:
    for line in lorem_ipsum_text:
        if 'mary' in line.lower():
            print(line,end='')

## заносим построчно в список
with open('E:\work\Python\python_course\sample.txt', 'r') as lorem_ipsum_text:
    lines = lorem_ipsum_text.readlines()
print(lines)
for line in lines[::-1]:
    print(line)

## текст в переменную без цикла
with open('E:\work\Python\python_course\sample.txt', 'r') as lorem_ipsum_text:
    text = lorem_ipsum_text.read()
print(text)



