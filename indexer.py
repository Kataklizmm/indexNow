import requests
import os
import key_gen
import json
from urllib.parse import urlparse

domain = input("Введите домен для которого хотите отправить запрос без протокола \n")
domain_key = domain.replace('.', '-')

for file in os.listdir():
    if file.startswith(domain_key):
        key = file[:-4]
        break
    else:
        key = ''
if not key:
    print('ключ не найден, запускаю генерацию нового ключа')
    key = key_gen.keygen(domain)
    input('В рабочей папке появился файл ключа. Закиньте сгенерированный файл в корень сайта, затем нажмите Enter\nЕсли не сделать это, вызовется ошибка')

if os.path.isfile('index.txt'):
    urls_list = list()
    file = open('index.txt', 'r', encoding='utf-8')
    urls = file.read()
    for i in urls.split('\n'):
        urls_list.append(i)
else:
    print("Файл index.txt не найден")

headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Host': 'yandex.com'
}

params = {
    "host": domain,
    "key": key,
    "urlList": urls_list
}

data=json.dumps(params)
resp = requests.post("https://yandex.com/indexnow", data=data)

print(resp.text)
print(resp.status_code)
if resp.status_code == 200:
    print("Запрос успешно отправлен")
