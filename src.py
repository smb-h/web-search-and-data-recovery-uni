import requests
from bs4 import BeautifulSoup
import __future__
import hazm

# https://github.com/smb-h/WSDR
# http://www.sobhe.ir/hazm/
# https://github.com/sobhe/hazm



# response = requests.get('https://fa.wikipedia.org/wiki/%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87_%D8%A2%D8%B2%D8%A7%D8%AF_%D8%A7%D8%B3%D9%84%D8%A7%D9%85%DB%8C_%D9%88%D8%A7%D8%AD%D8%AF_%DA%A9%D8%B1%D8%AC')
# print(response.status_code)
# print(response.content)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.p)

fl = open("data", "r")
data = fl.readlines()

normalizer = hazm.Normalizer()

print(data)
