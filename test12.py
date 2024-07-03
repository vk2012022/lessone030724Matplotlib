import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL для парсинга
url = 'https://www.divan.ru/category/divany'

# Заголовки для запроса, чтобы избежать блокировки
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Запрос на страницу
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Извлечение данных о диванах
products = soup.find_all('div', class_='product-card')
data = []

for product in products:
    name_tag = product.find('a', class_='product-card__name')
    price_tag = product.find('span', class_='product-card__price')

    if name_tag and price_tag:
        name = name_tag.text.strip()
        price = price_tag.text.strip()
        price = int(price.replace(' ', '').replace('₽', ''))
        data.append([name, price])

# Сохранение данных в CSV-файл
df = pd.DataFrame(data, columns=['Name', 'Price'])
df.to_csv('divan_prices.csv', index=False)
