import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://www.divan.ru/category/svet'
driver.get(url)
time.sleep(3)

items = driver.find_elements(By.CLASS_NAME, 'LlPhw')

parsed_data = []

for item in items:
    try:
        title_element = item.find_element(By.CLASS_NAME, 'name')
        title = title_element.text.strip()

        link_element = item.find_element(By.TAG_NAME, 'a')
        link = link_element.get_attribute('href')

        try:
            price = item.find_element(By.CLASS_NAME, 'ui-LD-ZU').text.strip()
        except:
                price = "Не указана"


        parsed_data.append([title, price, link])

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue


driver.quit()

with open("svet.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название товара','Цена товара', 'Ссылка на товар'])
    writer.writerows(parsed_data)



