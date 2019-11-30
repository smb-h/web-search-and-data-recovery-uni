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

# read from file
fl = open("data", "r")
data = fl.readlines()


# normaizer
normalized_data = []
normalizer = hazm.Normalizer()
for line in data:
    normalized_data.append(normalizer.normalize(line.strip()))


tokenized_data = []
for line in normalized_data:
    tmp = hazm.word_tokenize(line)
    if tmp:
        for token in tmp:
            tokenized_data.append(token)


print(tokenized_data)
