
* [] Oauth2 authentication.
* [] Test cases by classes, methods and packages.
* [] Implement databases for testing

### Authentication commands steps
Register a user for the first time.
```
curl -d "username=user1&password=strong_pass1" http://localhost:9000/user/register/
```
It gives you an access token ACCESS_TOKEN_HERE.

Login process.
```
curl -X POST http://localhost:9000/user/login/ -d "username=user1&password=strong_pass1"
```
ACCESS_TOKEN_HERE

Refresh token
```
curl -X POST http://localhost:9000/user/refresh/ -d "refresh_token=REFRESH_TOKEN_HERE"
```

Logout process
```
curl -X POST http://localhost:9000/user/logout/ -d "ACCESS_TOKEN_HERE"
```




PUT
curl --request PUT --url http://localhost:8080/put --header 'content-type: application/x-www-form-urlencoded' --data 'bar=baz&foo=foo1'

POST
curl --request POST --url http://localhost:8080/post --header 'content-type: application/x-www-form-urlencoded' --data 'bar=baz&foo=foo1'

GET
curl --request GET --url 'http://localhost:8080/get?foo=bar&foz=baz'
