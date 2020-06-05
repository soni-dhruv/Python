import pandas as pd
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt

#df = pd.read_csv('Workbook1.csv')
text ="jgh gj ygjg jtug ugt u huyb  iiyy giy gjhv jyhv jyy hsdthsry ad hjeatjrtj sjt jadhkrhgo nioraurhiu arhsgiou iuarsr gliasugf aisugsuig lasduugdasslghlareygo salkfgho  vyi vkh bky vbky vkh vk hvbkh vb kvb kb g kb kb kb kb i"
#text = text.to_string()
#text = 'hdfgdshjf hf djfj dkgfjkg'
wordcloud = WordCloud().generate(text)
wordcloud = WordCloud(max_font_size=30, max_words=100, background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()