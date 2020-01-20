import requests

"""
An HTTP client to get, create and delete items
"""


URL = 'http://127.0.0.1:5000'
data = {'Elena': 'The wise'}

# to create a name
response = requests.post(f'{URL}/names', json=data)
# to delete a name
# response = requests.delete(f'{URL}/names/Camilla')
# to get all names
# response = requests.get(f'{URL}/names')


# EXERCISE: how do you get a specific name?

print(f'Server replied with status {response.status_code} and data {response.content}')
