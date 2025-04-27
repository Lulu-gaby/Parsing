import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://www.divan.ru/category/svet'
driver.get(url)
time.sleep(5)

items = driver.find_elements(By.CSS_SELECTOR, 'Pk6w8')

parsed_data = []

for item in items:
    try:
        title_element = item.find_element(By.CLASS_NAME, 'oIrcb').text
        title = title_element.find_element(By.TAG_NAME, 'a').text
        link = title_element.find_element(By.TAG_NAME, 'a').get_attribute('href')

        try:
            item_type = item.find_element(By.CLASS_NAME, 'product-subtitle').text.strip()
        except:
            item_type = 'не указан'

        try:
            price = item.find_element(By.CLASS_NAME, 'ui-LD-ZU').text.strip()
        except:
                price = "Не указана"

        parsed_data.append([title, item_type, price, link])

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue


driver.quit()

with open("svet.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название товара', 'Вид прибора', 'Цена товара', 'Ссылка на товар'])
    writer.writerows(parsed_data)



