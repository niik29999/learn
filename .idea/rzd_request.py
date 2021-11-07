# список РГ
import requests
from bs4 import BeautifulSoup

response = requests.get('https://pass.rzd.ru/tickets/public/ru?STRUCTURE_ID=704&refererPageId=4819&layer_name=e3-route&tfl=3&st0=%D0%A7%D0%95%D0%91%D0%9E%D0%9A%D0%A1%D0%90%D0%A0%D0%AB&code0=2060620&dt0=13.08.2021&st1=%D0%9C%D0%9E%D0%A1%D0%9A%D0%92%D0%90&code1=2000000&checkSeats=1')
html_data = BeautifulSoup(response.text, 'html.parser')
print(html_data)
quotes = html_data.find_all(class_='col-xs-24 j-trains-col')
print(quotes)



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