import scrapy
import csv

class DivanlightsSpider(scrapy.Spider):
    name = "divanlights"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]
    parsed_data = []

    def parse(self, response):
        lights = response.css('div.H1U7L')
        print(f"Найдено товаров: {len(lights)}")

        for light in lights:
            item = {
                'Название товара': light.css('div.lsooF span::text').get(),
                'Цена товара':light.css('div.pY3d2 span::text').get(),
                'Ссылка на товар':light.css('a').attrib['href']
            }
            self.parsed_data.append(item)

    def closed(self, reason):
        with open("svet.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Название товара', 'Вид прибора', 'Цена товара', 'Ссылка на товар'])
            writer.writeheader()
            writer.writerows(self.parsed_data)
