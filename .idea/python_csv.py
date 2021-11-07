import csv

# чтение
with open('E:\work\Python\cars.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) 				# пропускаем заголовок
    for car in csv_reader:
        # print(car)
        print(f'{car[1]} {car[2]} costs {car[4]}')

with open('E:\work\Python\cars.csv') as file:
    csv_reader = csv.reader(file)
    data_list = list(csv_reader)
    print(data_list)

with open('E:\work\Python\cars.csv') as file:
	csv_reader = csv.DictReader(file)
	for car in csv_reader:
		# print(car)
		print(f'{car["make"]} {car["model"]} costs {car["price"]}')

with open('E:\work\Python\cars1.csv') as file:
	csv_reader = csv.DictReader(file,delimiter=";")
	for car in csv_reader:
		# print(car)
		print(f'{car["make"]} {car["model"]} is {car["year"]} m')

with open('E:\work\Python\cars1.csv') as file:
	csv_reader = csv.reader(file,delimiter=";")
	next(csv_reader)
	for car in csv_reader:
		# print(car)
		print(f'{car[1]} {car[2]} is {car[3]} m')

# запись
with open('students.csv', 'w') as file:
	csv_writer = csv.writer(file)
	csv_writer.writerow(['First name', 'Last name', 'Age'])
	csv_writer.writerow(['Jack', 'White', 24])
	csv_writer.writerow(['Jane', 'Black', 23])

# чтение из одного csv  и запись в другой использую list
with open('cars.csv') as file:
	csv_reader = csv.reader(file)
	next(csv_reader)
	make_model_list = []
	for car in csv_reader:
		make_model = [car[1], car[2]]
		make_model_list.append(make_model)
	print(make_model_list)

with open('cars_make_model.csv', 'w') as file:
	csv_writer = csv.writer(file)
	for row in make_model_list:
		csv_writer.writerow(row)

# одновременное чтение из одного файла и запись в другой csv
with open('cars.csv') as file:
	csv_reader = csv.reader(file)
	next(csv_reader)
	# make_model_list = []

	with open('cars_make_model.csv', 'w') as file:
		csv_writer = csv.writer(file)
		for row in csv_reader:
			csv_writer.writerow([row[1], row[2]])

# запись с использование словаря
with open('students1.csv','w') as file:
	headers_list = ['First name', 'Last name', 'Age']
	csv_writer = csv.DictWriter(file, fieldnames=headers_list)
	csv_writer.writeheader()
	csv_writer.writerow({
		'First name':'Jack',
		'Last name':'White',
		'Age':24
	})
	csv_writer.writerow({
		'First name':'Jane',
		'Last name':'Black',
		'Age':23
	})

# чтение из одного csv  и запись в другой использую list и словарь
with open('cars.csv') as file:
	csv_reader = csv.DictReader(file)
	car_list = list(csv_reader)
# print(car_list)

with open('make_model.csv', 'w') as file:
	headers_list = ['Make', 'Model']
	csv_writer = csv.DictWriter(file, fieldnames=headers_list)
	csv_writer.writeheader()
	for car in car_list:
		csv_writer.writerow({
			'Make': car['Make'],
			'Model': car['Model']
		})

# занесение результатов веб скрапинга в csv файл
import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('http://quotes.toscrape.com/')
html_data = BeautifulSoup(response.text)
quotes = html_data.find_all(class_='quote')

with open('quotes.csv', 'w') as file:
	csv_writer = writer(file)
	csv_writer.writerow(['Text', 'Author', 'Keywords'])

	for quote in quotes:
		text = quote.find(class_='text').get_text()
		author = quote.find(class_='author').get_text()
		keywords = quote.find(class_='keywords')['content']
		csv_writer.writerow([text, author, keywords])


		