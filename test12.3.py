import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib.pyplot as plt

# Настройка Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Запуск в фоновом режиме
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Открытие страницы
url = 'https://www.divan.ru/category/divany'
driver.get(url)
time.sleep(5)  # Ожидание загрузки страницы

# Парсинг данных о диванах
data = []

# Используем XPath для поиска элементов
products = driver.find_elements(By.CLASS_NAME, 'wYUX2')

for product in products:
    try:
        name = product.find_element(By.CLASS_NAME, 'ProductName').text
        price = product.find_element(By.XPATH, './/span[@data-testid="price"]').text
        price = int(price.replace(' ', '').replace('руб.', ''))
        data.append([name, price])
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        continue

# Закрытие браузера
driver.quit()

# Сохранение данных в CSV-файл
df = pd.DataFrame(data, columns=['Name', 'Price'])
df.to_csv('divan_prices.csv', index=False)

# Проверка содержимого DataFrame
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

# Нахождение средней цены
average_price = df['Price'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} руб.')

# Построение гистограммы цен
plt.hist(df['Price'], bins=30, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (руб)')
plt.ylabel('Количество')
plt.show()
