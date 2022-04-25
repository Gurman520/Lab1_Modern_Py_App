from requests import post, get, delete, put

print(get('http://localhost:5000/api/v2/users').json())
