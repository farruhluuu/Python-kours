# import requests
# from bs4 import BeautifulSoup


# URL = 'https://limon.kg/ru'

# text = requests.get(URL)
# print(text.text)
# soup = BeautifulSoup(text.text, 'html.parser')

# title = soup.find('a',{'class': 'journal_itme_name'})
# print(title)

 
# import requests
# from bs4 import BeautifulSoup


# URL = 'https://lalafo.kg/'

# text = requests.get(URL)

# soup = BeautifulSoup(text.text, 'html.parser')

# card = soup.find('div', {'class':'adTile-mainInfo'})

# if card.find('p', {'class':'adTile-price'}):
#     price_div = card.find('p', {'class':'adTile-price'})
#     price = card.find('span')
# else:
#     price = card.find('p', {'class':'adTile-price'})
# title = card.find('div', {'class':'adTile-title__wrap'})
  

# print(title.text)
# print(price.text)


