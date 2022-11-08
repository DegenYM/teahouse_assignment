import requests

host = 'http://127.0.0.1:12345'
inputs = {'mean':10, 'std_dev':10, 'arr_len':10}

response = requests.post( host+'/sampling', data=inputs)
# response = requests.get( host+'/sampling', params=inputs)
output = response.json()

print(output)