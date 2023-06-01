'''
Эта музыка будет вечной

Полина хочет познакомиться с музыкой новой группы, послушав какие-нибудь три её песни. Помогите Полине выбрать, указав три наиболее прослушиваемые песни группы по данным стриминговых сервисов.

ФОРМАТ ВВОДА

Строка с адресом страницы со статистикой.
Гарантируется, что количество воспроизведений каждой песни уникально и все названия песен уникальны, что песен в таблице больше, чем 3.
ФОРМАТ ВЫВОДА

3 строки с названиями песен, упорядоченными по рейтингу
Страницу, анализируемую в открытом тесте, можно посмотреть здесь.

При отправке задачи в функцию BeautifulSoup() нужно передать второй аргумент: 'lxml'.

Например, вместо кода soup = BeautifulSoup(page.text) нужно написать soup = BeautifulSoup(page.text, 'lxml')
'''

import requests
from bs4 import BeautifulSoup

url = input()
page = requests.get(url)

page.encoding = 'utf-8'

soup = BeautifulSoup(page.text,  'lxml')

td = soup.find_all('td')

dictionary = {}

for i in range(len(td)):
    if i % 2 == 0:
        dictionary[td[i].text] = td[i+1].text

sorted_dict = sorted(dictionary.items(), key=lambda value: int(value[1]))
three_first = sorted_dict[:1:-1]
print(three_first[0][0], three_first[1][0], three_first[2][0], sep='\n')
