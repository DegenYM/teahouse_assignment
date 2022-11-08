# Question 4
Backend framework: Flask
## Requirements 
* python 3.6+
* flask 
* web3
* requests

## Step1. Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the  packges.

```bash
pip install -r requirements.txt
```

## Step 2. Run backend server
Default host = 127.0.0.1, port = 22345

```bash
python3 server.py
```

## Step 3. API Usage
You can use `GET` or `POST` methods to send the request to server. The binded URL of the function is http://127.0.0.1:22345/get_balance. The function has two inputs: `token_address, query_address`.  
### 1. GET method
Using `GET` to send the request, you can pass the parameters from URL. For example, enter URL http://127.0.0.1:22345/get_balance?token_address=0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48&query_address=0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045, then you will get the output json.

### 2. POST method
Using `POST` to send the request, you can pass the inputs from argsparse.
#### Sample call
```python

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

```
In terminal, type the following command:
``` bash
>>> python3 sample_call.py -token_address 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 -query_address 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
```
results:
```
>>> token_address
'0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
>>> query_address
'0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
>>> output
{'query_address': '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045', 'query_balance': 31201.786744, 'query_raw_balance': 31201786744, 'token_address': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', 'token_name': 'USDC'}
```