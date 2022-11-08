# Question 2
Backend framework: Flask
## Requirements
* python 3.5+
* flask 
* requests

## Step 1. Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packges.

```bash
pip install -r requirements.txt
```
## Step 2. Run backend server

Default host = 127.0.0.1, port = 12345

```bash
python3 server.py
```
## Step 3. API Usage
You can use `GET` or `POST` methods to send the request to server. The binded URL of the function is http://127.0.0.1:12345/sampling. The function has three inputs: `mean, std_dev, arr_len`.  
### 1. GET method
Using `GET` to send the request, you can pass the parameters from URL. For example, enter URL http://127.0.0.1:12345/sampling?mean=10&std_dev=10&arr_len=10, then you will get the output list.

### 2. POST method
Using `POST` to send the request, you can pass the inputs from argsparse.
#### Sample call
```python
import requests
import argparse

host = 'http://127.0.0.1:12345'
parser = argparse.ArgumentParser()
parser.add_argument("-mean", type=float)
parser.add_argument("-std_dev", type=float)
parser.add_argument("-arr_len", type=int)
args = parser.parse_args()

inputs = {'mean':args.mean, 
        'std_dev':args.std_dev, 
        'arr_len':args.arr_len}

# You can send the request from GET or POST method.
response = requests.post(host+'/sampling', data=inputs)
# response = requests.get( host+'/sampling', params=inputs)

output = response.json()
```
In terminal, type the following command:
``` bash 
>>> python3 sample_call.py -mean 10 -std_dev 10 -arr_len 10
```
results:
```
>>> output
[16.254706033237593, 15.973333813859123, 7.369759138114892, 9.968129331749525, 12.553171674082938, 13.367798266730645, 0.7945944852345566, 5.776632393176249, 7.863799729126285, 8.98648357904143]
```
