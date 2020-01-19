import requests


URL = 'http://127.0.0.1:500'
# data = {'Elena': 'the wise'}

# res = requests.post('http://127.0.0.1:5000/names', json=data)
# print(res.status_code)

requests.delete('http://127.0.0.1:5000/names/Camilla')
