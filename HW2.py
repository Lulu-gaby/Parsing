import requests
import pprint

params = {
    "userId": 1
}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

if response.status_code == 200:
    posts = response.json()
    pprint.pprint(posts)
else:
    print(f"Ошибка! Статус-код: {response.status_code}")