import __future__
import hazm


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
# [('ما', 'PRO'), ('بسیار', 'ADV'), ('کتاب', 'N'), ('می‌خوانیم', 'V')]


# Chunker
# chunker = hazm.Chunker(model='resources/chunker.model')
# tagged = tagger.tag(word_tokenize('کتاب خواندن را دوست داریم'))
# tree2brackets(chunker.parse(tagged))
# '[کتاب خواندن NP] [را POSTP] [دوست داریم VP]'


# Parser
# parser = DependencyParser(tagger=tagger, lemmatizer=lemmatizer)
# parser.parse(word_tokenize('زنگ‌ها برای که به صدا درمی‌آید؟'))
# <DependencyGraph with 8 nodes>
