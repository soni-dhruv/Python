#APIs

import requests
import json
url = 'https://reqres.in/api/users'
data = requests.get(url)
plainText = data.text

res = json.loads(plainText)

for i in res['data']:
    print(i['first_name'])
"""
print(res['data'][0]['first_name'])
print(res['data'][0]['last_name'])
"""

    
