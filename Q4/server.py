from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/ee96256c1e6643e39b8e6cd27d471e73"))

@app.route('/')
def hello():
    return 'Hello TeaHouse'

@app.route('/get_balance', methods=['GET', 'POST'])
def get_balance():
    if request.method == 'GET':
        contract_abi = request.args.get('abi')
        token_address = request.args.get('token_address')
        query_address = request.args.get('query_address')

    elif request.method == 'POST':
        contract_abi = request.form['abi']
        token_address = request.form['token_address']
        query_address = request.form['query_address']
    
    token = w3.eth.contract(address=token_address, abi=contract_abi)
    token_name = token.functions.symbol().call()
    token_balance = token.functions.balanceOf(query_address).call()
    decimals = token.functions.decimals().call()

    output = {'Token name': token_name, 
            'Token address': token_address, 
            'Query address': query_address,
            'Query balance': token_balance/(10**decimals)}

    return jsonify(output)

if __name__ == '__main__':
    init_host = '127.0.0.1'
    app.run(host=init_host,port=22345)
