import requests

"""
An HTTP client to get, create and delete items
"""


URL = 'http://127.0.0.1:5000'
data = {'Elena': 'A pan-European version of Helen, has roots in Spanish, Italian, Slavic, and Romanian, among others.'
                 'Helen, the name from which it derives, came from the Greek word helene, meaning “torch.”'}

# to create a name
# response = requests.post(f'{URL}/names', json=data)

# to delete a name
# response = requests.delete(f'{URL}/names/Camilla')

# to get all names
# response = requests.get(f'{URL}/names')

# print(f'Server replied with status {response.status_code} and data {response.content}')

# EXERCISE: how do you get a specific name?
