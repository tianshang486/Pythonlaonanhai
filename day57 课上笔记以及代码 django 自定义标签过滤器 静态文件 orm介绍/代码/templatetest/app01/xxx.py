import requests
ret = requests.post('http://127.0.0.1:8000/login/',data={
    'username':'dazuang',

})

print(ret.text)










