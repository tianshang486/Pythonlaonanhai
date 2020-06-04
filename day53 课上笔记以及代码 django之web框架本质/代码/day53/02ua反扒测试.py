
import requests

# res = requests.get('https://www.jd.com/2019')
res = requests.get('https://dig.chouti.com/',headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
})
# print(res.content)

with open('ct.html','w',encoding='utf-8') as f:
    f.write(res.text)













