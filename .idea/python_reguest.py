# HTTP
import requests

url = 'https://www.yandex.ru'
response = requests.get(url)
print(f'Request to {url}. Status code is {response.status_code}.')
print(response.text)

# API
import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept':'application/json'}, params={
    'format':'geojson',
    'starttime':'2019-01-01',
    'endtime':'2019-05-01',
    'latitude':'51.51',
    'longitude':'-0.12',
    'maxradiuskm':'2000'

})
# print(response.text)
# print(type(response.json()))
# print(type(response.text))

data = response.json()
print(data['features'][1]['properties']['place'])

# извлечение данных
from bs4 import BeautifulSoup
html_string = """
	<!DOCTYPE html>
	<html>
	<head>
		<title>Web Development Page</title>
		<style type="text/css">
			
			h1{
				color: white;
				background: red;
			}

			li{
				color: red;
			}

			#css-li{
				color: blue;
			}

			.green{
				color: green;
			}

		</style>
	</head>
	<body>
		<h1>Web Development</h1>
		<h1 class="green">Web</h1>
		<h3>Programming Languages</h3>

		<ol>
			<li>HTML</li>
			<li id="css-li">CSS</li>
			<li class="green bold">JavaScript</li>
			<li class="green" id="python-li">Python</li>
		</ol>

	</body>
	</html>



"""

parsed_html = BeautifulSoup(html_string, 'html.parser')

# print(parsed_html.body.ol.li)
# print(parsed_html.find('li'))
# print(type(parsed_html.find('li')))
# print(parsed_html.find_all('li'))
# print(type(parsed_html.find_all('li')))
# print(parsed_html.find(id="css-li"))
# print(parsed_html.select('#css-li')[0])
# print(parsed_html.find_all(class_="green"))
# print(parsed_html.select(".green")[1])
# print(parsed_html.select("li")[3])
# html_elem = parsed_html.select("li")[0]
# print(html_elem.get_text())

# html_elem_list = parsed_html.select("li")

# for html_elem in html_elem_list:
# 	print(html_elem.get_text())

# green_class_elem_list = parsed_html.select("li")

# for html_elem in green_class_elem_list:
# 	print(html_elem.get_text())

# for html_elem in green_class_elem_list:
# 	print(html_elem.attrs)

html_elem_list = parsed_html.select("li")[3]
# print(html_elem_list.attrs['id'])
print(html_elem_list['class'])

# data = parsed_html.body.contents[1].next_sibling.next_sibling.next_sibling.next_sibling
# data = parsed_html.find(id="css-li").parent.previous_sibling.previous_sibling
# data = parsed_html.find(id="css-li").find_next_sibling().find_previous_sibling()
# data = parsed_html.find(id="css-li").find_next_sibling(id="python-li")
# data = parsed_html.find(id="css-li").find_next_sibling(class_="bold")
# data = parsed_html.find(id="css-li").find_next_sibling(class_="bold").find_parent().find_parent()
data = parsed_html.body.findChildren()[2].find_next_sibling()
print(data)

#web scrapping
# http://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com/')
html_data = BeautifulSoup(response.text)
quotes = html_data.find_all(class_='quote')
for quote in quotes:
    print(quote.find(class_='text').get_text())
    print(quote.find(class_='author').get_text())
    print(quote.find(class_='keywords')['content'])

# список проектов ПИК
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.pik.ru/projects')
html_data = BeautifulSoup(response.text, 'html.parser')
quotes = html_data.find_all(class_='sc-hrZbnf iYxjkl')
#print(quotes)
for quote in quotes:
    print("https://www.pik.ru" + quote.attrs['href'])
    print(quote.find(class_="sc-bdfBwQ iCEAmZ Typography").get_text())
    print(quote.find(class_="sc-bdfBwQ joxDrc Typography").get_text())
    if quote.find(class_="sc-bdfBwQ jUztQR Typography") is None:
        print("None")
    else: print(quote.find(class_="sc-bdfBwQ jUztQR Typography").get_text())

# список РГ
import requests
from bs4 import BeautifulSoup

response = requests.get('https://rg-dev.ru/flats/?complex=b0dbb09f-3c7b-eb11-8118-00155df44d2f&rooms=0,1')
html_data = BeautifulSoup(response.text, 'html.parser')
quotes = html_data.find_all(class_='flat-card__info-row')
# print(quotes)
for quote in quotes:
    # print("https://www.pik.ru" + quote.attrs['href'])
    if quote.find(class_="flat-card__val _small fw-m") is None:
        print("None")
    else: print(quote.find(class_="flat-card__val _small fw-m").get_text().strip())
    if quote.find(class_="flat-card__val _small") is None:
        print("None")
    else: print(quote.find(class_="flat-card__val _small").get_text().strip())
    if quote.find(class_="flat-card__val c-red fw-sb") is None:
        print("None")
    else: print(quote.find(class_="flat-card__val c-red fw-sb").get_text().strip())

