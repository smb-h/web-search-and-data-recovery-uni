import requests
from bs4 import BeautifulSoup
import __future__
import hazm
import re
import pandas as pd


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
str_data = " ".join(o for o in data)


# normaize data
normalized_data = []
normalizer = hazm.Normalizer()
for line in data:
    normalized_data.append(normalizer.normalize(line.strip()))


stemmer = hazm.Stemmer()
lemmatizer = hazm.Lemmatizer()

# tokenize, stem and lemmatize data
processed_data = []
for line in normalized_data:
    tmp = hazm.word_tokenize(line)
    if tmp:
        for token in tmp:
            curr_word = stemmer.stem(token)
            # curr_word = lemmatizer.lemmatize(token)
            processed_data.append(curr_word)


# sort processed data
processed_data.sort()

temp = []
for i in processed_data:
    if i not in temp:
        temp.append(i)

processed_data = temp

position_list = []
# positions
for wd in processed_data:
    counter = str_data.count(wd)
    pos = 0
    tmp = []
    for count in range(counter):
        indx = str_data.find(wd, pos)
        pos += indx + len(wd)
        if pos not in tmp:
            tmp.append(pos)
    position_list.append(tmp)

# position_list_formated = []
# for i in position_list:
#     tmp = ""
#     for j in i:
#         tmp = tmp + str(j) + ", "
#     position_list_formated.append(tmp)


# write processed data into csv file
format_data = {
    'words': processed_data,
    'positions': position_list
}
data_frame = pd.DataFrame(format_data)
data_frame.to_csv("processed_data.csv", sep=",", encoding='utf-8')


