from requests import post, get, delete, put

# Тесты на поиск нужной записи
print(get('http://localhost:5000/api/jobs').json())  # Получение всех записей
print(get('http://localhost:5000/api/jobs/3').json())  # Получение одной записи
print(get('http://localhost:5000/api/jobs/999').json())  # Ошибочный запрос
print(get('http://localhost:5000/api/jobs/"2"').json())  # Ошибочный запрос

# Тесты на создание записи
print(post('http://localhost:5000/api/jobs', json={}).json())
print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1}).json())
print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1,
                 'job': "Test_string",
                 'work_size': 2,
                 'is_finished': False}).json())

# Тесты на удаление записей
print(delete('http://localhost:5000/api/jobs/999').json())
print(delete('http://localhost:5000/api/jobs/5').json())

# Тесты на изменение данных
print(put('http://localhost:5000/api/jobs/4', json={'is_finished': True}).json())
