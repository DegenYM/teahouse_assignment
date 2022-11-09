from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/ee96256c1e6643e39b8e6cd27d471e73"))

def abort_msg(e):
    error_class = e.__class__.__name__ # error class
    detail = e.args[0]

    # generate the error message
    errMsg = "[{}] {}.".format(error_class, detail)
    # return 500 code
    abort(500, errMsg)
    
@app.route('/')
def hello():
    return 'Hello TeaHouse'

@app.route('/get_balance', methods=['GET', 'POST'])
def get_balance():
    contract_abi = '[{"constant": true,"inputs": [],"name": "name","outputs": [{"name": "","type": "string"}],"payable": false,"type": "function"}, {"constant": true,"inputs": [],"name": "decimals","outputs": [{"name": "","type": "uint8"}],"payable": false,"type": "function"},{"constant": true,"inputs": [{"name": "_owner","type": "address"}],"name": "balanceOf","outputs": [{"name": "balance","type": "uint256"}],"payable": false,"type": "function"},  {"constant": true,"inputs": [],"name": "symbol","outputs": [{"name": "","type": "string"}],"payable": false,"type": "function"}]'

    if request.method == 'GET':
        token_address = request.args.get('token_address')
        query_address = request.args.get('query_address')

    elif request.method == 'POST':
        token_address = request.form['token_address']
        query_address = request.form['query_address']
    try:
        token = w3.eth.contract(address=token_address, abi=contract_abi)
        token_name = token.functions.symbol().call()
        token_balance = token.functions.balanceOf(query_address).call()
        decimals = token.functions.decimals().call()

        output = {'token_name': token_name, 
                'token_address': token_address, 
                'query_address': query_address,
                'query_raw_balance': token_balance, 
                'query_balance': token_balance/(10**decimals)}

        return jsonify(output)

       except Exception as e:
            abort_msg(e)
            
if __name__ == '__main__':
    init_host = '127.0.0.1'
    app.run(host=init_host,port=22345)
