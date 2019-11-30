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
normalizer = hazm.Normalizer()
# normalizer.normalize('اصلاح نويسه ها و استفاده از نیم‌فاصله پردازش را آسان مي كند')
# 'اصلاح نویسه‌ها و استفاده از نیم‌فاصله پردازش را آسان می‌کند'


# sentence tokenizer
# hazm.sent_tokenize('ما هم برای وصل کردن آمدیم! ولی برای پردازش، جدا بهتر نیست؟')
# ['ما هم برای وصل کردن آمدیم!', 'ولی برای پردازش، جدا بهتر نیست؟']

# word tokenizer
# hazm.word_tokenize('ولی برای پردازش، جدا بهتر نیست؟')
# ['ولی', 'برای', 'پردازش', '،', 'جدا', 'بهتر', 'نیست', '؟']


# Stemmer
stemmer = hazm.Stemmer()
# stemmer.stem('کتاب‌ها')
# 'کتاب'


# Lemmatizer
lemmatizer = hazm.Lemmatizer()
# lemmatizer.lemmatize('می‌روم')
# 'رفت#رو'


# Tagger
# tagger = hazm.POSTagger(model='resources/postagger.model')
# tagger.tag(hazm.word_tokenize('ما بسیار کتاب می‌خوانیم'))


# Chunker
# chunker = hazm.Chunker(model='resources/chunker.model')
# tagged = tagger.tag(word_tokenize('کتاب خواندن را دوست داریم'))


# Parser
# parser = DependencyParser(tagger=tagger, lemmatizer=lemmatizer)
# parser.parse(word_tokenize('زنگ‌ها برای که به صدا درمی‌آید؟'))
