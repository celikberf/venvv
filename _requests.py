import requests
import json

result = requests.get('https://jsonplaceholder.typicode.com/todos')
result = json.loads(result.text) # adres üzerindn gelen bilgileri aldık


for i in result:
    if i['userId'] == 1:
        print(i['title']) # her gelen kaydın sadece title bilgisi

