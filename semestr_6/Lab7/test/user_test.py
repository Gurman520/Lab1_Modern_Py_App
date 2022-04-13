from requests import post, get, delete, put

# Тесты на поиск нужной записи
print(get('http://localhost:5000/api/user').json())  # Получение всех записей
print(get('http://localhost:5000/api/user/3').json())  # Получение одной записи
print(get('http://localhost:5000/api/user/999').json())  # Ошибочный запрос
print(get('http://localhost:5000/api/user/"2"').json())  # Ошибочный запрос

# Тесты на создание записи
print(post('http://localhost:5000/api/user', json={}).json())
print(post('http://localhost:5000/api/user',
           json={'age': 1}).json())
print(post('http://localhost:5000/api/user',
           json={'name': 'Roman', 'surname': 'Sulima', 'age': 20, 'position': 'Capitan',
                 'email': 'capitan_roman@gmail.com'}).json())

# Тесты на удаление записей
print(delete('http://localhost:5000/api/user/999').json())
print(delete('http://localhost:5000/api/user/10').json())

# Тесты на изменение данных
# print(put('http://localhost:5000/api/user/9', json={'is_finished': True}).json())
