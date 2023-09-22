### Overview
This is an unofficial Python wrapper for the [Coincall exchange API](https://docs.coincall.com)

If you came here looking to purchase cryptocurrencies from the Coincall exchange, please go [here](https://www.coincall.com/).

#### Source code
https://github.com/Coincall-exchange/python-coincall

### Features
- Implementation of all Rest API endpoints.

### Quick start
#### Prerequisites

`python version：>=3.9`

`WebSocketAPI： websockets package advise version 6.0`

#### Step 1: register an account on Coincall and apply for an API key
- Register for an account: https://www.coincall.com/signup
- Apply for an API key: https://www.coincall.com/account/apikeys

#### Step 2: install python-coincall

```python
pip install python-coincall
```

#### Step 3: Run examples

- availabel modules
```python 
from coincall import User, Public, Futures, Options, Referral
```

- fill in API credentials when use a module with a SIGNED endpoint:
```python
api_key = 'Your API Key'
api_secret_key = 'Your API Secret'
```

- public module usage:
```python
publicApi = Public.PublicAPI()
print(publicApi.get_server_time())
```

- SIGNED endpoint module:
```python
userApi = User.UserAPI(api_key, api_secret_key)
print(userApi.get_user_info())
```