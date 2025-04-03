from bs4 import BeautifulSoup
from googletrans import Translator
import requests

def get_english_words():
    url = "http://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")


def word_game():
    print("Добро пожаловать в игру!")
    translator = Translator()

    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        transtaled_word = translator.translate(word,scr="eng", dest="ru").text
        translated_definition = translator.translate(word_definition, scr="eng", dest="ru").text

        print (f"Значение слова - {translated_definition}")
        user = input("Что это за слово? (введите на русском) ")
        if user == transtaled_word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {transtaled_word}")

        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()



