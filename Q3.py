from web3 import Web3
import json
import argparse

# Use the following command to run the script:
# python3 -query_address {str} -token_address {str}
# For example, if we want to query the balance of USDC from vitalik.eth, type the command: 
# python3 Q3.py -token_address 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 -query_address 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045

def get_balance(token_address: str, query_address: str):
    token = w3.eth.contract(address=token_address, abi=contract_abi)
    token_name = token.functions.symbol().call()
    token_balance = token.functions.balanceOf(query_address).call() 
    decimals = token.functions.decimals().call()

    return {'token_name': token_name, 
            'token_address': token_address, 
            'query_address': query_address,
            'query_raw_balance': token_balance, 
            'query_balance': token_balance/(10**decimals)}

if __name__ == '__main__':
    w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/ee96256c1e6643e39b8e6cd27d471e73"))
    # print(w3.isConnected())

    parser = argparse.ArgumentParser()
    parser.add_argument("-query_address", type=str)
    parser.add_argument("-token_address", type=str)
    args = parser.parse_args()

    # You can pass the ABI from external JSON file, or input ABI as a string. 
    contract_abi = '[{"constant": true,"inputs": [],"name": "name","outputs": [{"name": "","type": "string"}],"payable": false,"type": "function"}, {"constant": true,"inputs": [],"name": "decimals","outputs": [{"name": "","type": "uint8"}],"payable": false,"type": "function"},{"constant": true,"inputs": [{"name": "_owner","type": "address"}],"name": "balanceOf","outputs": [{"name": "balance","type": "uint256"}],"payable": false,"type": "function"},  {"constant": true,"inputs": [],"name": "symbol","outputs": [{"name": "","type": "string"}],"payable": false,"type": "function"}]'

    # USDC ERC20 = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
    token_address = args.token_address
    # vitalik.eth = 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
    query_address = args.query_address
    
    print(get_balance(token_address, query_address))
