from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.devtools.v85.dom import get_attributes

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

assert "Википедия" in browser.title
print("Добро пожаловать на страницу Википедия")

user_request = input("Введите запрос для поиска: ")

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(user_request)
search_box.send_keys(Keys.RETURN)
time.sleep(3)

def list_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        user_input = input("\nНажмите Enter для следующего параграфа или 'q' для выхода: ")
        if user_input == 'q':
            return

def follow_link():
    inside_links = []
    for link in browser.find_elements(By.TAG_NAME, "a"):
        href = link.get_attribute("href")
        if href and "/wiki/" in href:
            inside_links.append((link.text, href))

    print("\nДоступные ссылки:")
    for i, (text, href) in enumerate(inside_links[:5]):
        print(f"{i + 1}. {text} - {href}")

    choice = input("Выберите номер ссылки или 'q' для выхода: ")

    if choice == 'q':
        return

    try:
        choice = int(choice)
        if 0 < choice <= len(inside_links):
           browser.get(inside_links[choice - 1][1])
        time.sleep(3)

    except ValueError:
        print("Некорректный ввод, попробуйте снова.")

while True:
    print("\n1. Листать параграфы\n2. Перейти на связанную страницу\n3. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        list_paragraphs()
    elif choice == "2":
        follow_link()
    elif choice == "3":
        print("Выход из программы.")
        browser.quit()
        break
    else:
        print("Некорректный ввод, попробуйте снова.")