# Question 2
Backend framework: Flask
## Requirements
* python 3.5+
* flask 
* requests

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packges.

```bash
pip install flask
pip install requests
```
## 1. Run backend server

Default host = 127.0.0.1, port = 12345

```bash
python3 server.py
```

## API Usage
The binded URL of the function is http://127.0.0.1:12345/sampling.  You can use `GET` or `POST` methods to send the request.  
Request needs the input parameters with a `JSON` or `DICT` of following keys: `mean, std_dev, arr_len`. You can get the output list with `response.json()`.

## Sample call
```python
import requests

host = 'http://127.0.0.1:12345'

inputs = {'mean':10, 'std_dev':10, 'arr_len':100}

# You can use both GET or POST methods 
response = requests.post( host+'/sampling', data=inputs)
# response = requests.get( host+'/sampling', params=inputs)

output_elements = response.json()
```
``` bash 
>>> output_elements
[16.254706033237593, 15.973333813859123, 7.369759138114892, 9.968129331749525, 12.553171674082938, 13.367798266730645, 0.7945944852345566, 5.776632393176249, 7.863799729126285, 8.98648357904143]
```
