#Web Scraping

import requests
from bs4 import BeautifulSoup

for i in range(1,21):
    url = "https://www.flipkart.com/search?q=books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&page="+str(i)

    data = requests.get(url)
    #print(data)
    plain_text = data.text

    soup = BeautifulSoup(plain_text, 'html.parser')

    res = soup.findAll('a',{'class':'_2cLu-l'})
    #print(res)
    """
    for link in res:
        #print(link.get('title'))
        print(link.text.strip())
        print('-'*70)
    """


    rate = soup.findAll('div',{'class':'_1vC4OE'})
    for link in rate:
        #print(link.get('title'))
        print(link.text.strip())
        print('-'*10)


"""
.strip doest the work of print from openinig tag to closing tag
"""

