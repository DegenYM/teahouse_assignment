import requests
import argparse

host = 'http://127.0.0.1:12345'
parser = argparse.ArgumentParser()
parser.add_argument("-mean", type=float)
parser.add_argument("-std_dev", type=float)
parser.add_argument("-arr_len", type=int)
args = parser.parse_args()

inputs = {'mean':args.mean, 'std_dev':args.std_dev, 'arr_len':args.arr_len}

response = requests.post(host+'/sampling', data=inputs)
# response = requests.get( host+'/sampling', params=inputs)
output = response.json()

print(output)