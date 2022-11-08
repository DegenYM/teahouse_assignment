import requests
from web3 import Web3
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-query_address", type=str)
parser.add_argument("-token_address", type=str)
args = parser.parse_args()

# USDC ERC20 = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
token_address = args.token_address
# vitalik.eth = 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
query_address = args.query_address


contract_abi = '[{"constant": true,"inputs": [],"name": "name","outputs": [{"name": "","type": "string"}],"payable": false,"type": "function"}, {"constant": true,"inputs": [],"name": "decimals","outputs": [{"name": "","type": "uint8"}],"payable": false,"type": "function"},{"constant": true,"inputs": [{"name": "_owner","type": "address"}],"name": "balanceOf","outputs": [{"name": "balance","type": "uint256"}],"payable": false,"type": "function"},  {"constant": true,"inputs": [],"name": "symbol","outputs": [{"name": "","type": "string"}],"payable": false,"type": "function"}]'

inputs = {'token_address': token_address,
        'query_address': query_address}

host = 'http://127.0.0.1:22345'
response  = requests.post(host + '/get_balance', data=inputs)
print(response.json())
