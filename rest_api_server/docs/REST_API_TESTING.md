# REST API testing

## REST API call reference with curl
If you want to test the server use curl as following:

### Authentication commands steps
Register a user for the first time.
```
curl -d "username=user1&password=strong_pass1" http://localhost:9000/users/register/
```
It gives you an access token ACCESS_TOKEN_HERE and a REFRESH_TOKEN_HERE.

Login process.
```
curl -X POST http://localhost:9000/users/login/ -d "username=user1&password=strong_pass1"
```
ACCESS_TOKEN_HERE

Refresh token.
```
curl -X POST http://localhost:9000/users/refresh/ -d "refresh_token=REFRESH_TOKEN_HERE"
```
Test for valid grant, test for invalid grant


curl -X POST http://localhost:9000/users/logout/ -d "token=Vm8qU8vLcri8SiDp1hTv2BUtvHO4mj"
Logout process.
```
curl -X POST http://localhost:9000/users/logout/ -d "token=ACCESS_TOKEN_HERE"
```


### /commands/
```
curl -H "Authorization: Bearer A_TOKEN_HERE" http://localhost:9000/v1/commands/
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "command=START_RECORD" http://localhost:9000/v1/commands/
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "command=STOP_RECORD" http://localhost:9000/v1/commands/
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "command=WAITING" http://localhost:9000/v1/commands/
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "command=STOP_REMOTE_CLIENT" http://localhost:9000/v1/commands/
```

### /config/
```
curl -H "Authorization: Bearer A_TOKEN_HERE" http://localhost:9000/v1/config/
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "sleep_time=5" http://localhost:9000/v1/config/
```

### /executed/
```
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "command=RECORDING_ACK&start_record=''" http://localhost:9000/v1/commands/
curl -H "Authorization: Bearer A_TOKEN_HERE" http://localhost:9000/v1/command/1/
```

### /remote/
```
curl -H "Authorization: Bearer A_TOKEN_HERE" http://localhost:9000/v1/remote/
curl -H "Authorization: Bearer A_TOKEN_HERE" -d "uuid=IIUUII&hostname=UNOHOST&os='WINDOWS'&ip='192.168.0.1'" http://localhost:9000/v1/remote/
```

## Authorship
This project is contributed by .

## Citation
If you find this code useful, please consider citing:
...
