from requests import post, get, delete, put
import pytest


# Тесты на поиск нужной записи

def test_get_user():
    map = {'user': [
        {'age': 21, 'email': 'scott_chief@mars.org', 'name': 'Ridley', 'position': 'captain', 'surname': 'Scott'},
        {'age': 25, 'email': 'Omar@mars.org', 'name': 'Omar', 'position': 'engineer', 'surname': 'Eps'},
        {'age': 29, 'email': 'pilot_master_Vil@mars.org', 'name': 'Ridley', 'position': 'pilot', 'surname': 'Vilsan'},
        {'age': 40, 'email': 'Greg_H@mars.org', 'name': 'Greg', 'position': 'engineer', 'surname': 'House'},
        {'age': 24, 'email': 'forman_doctor@mars.org', 'name': 'Eric', 'position': 'chief doctor', 'surname': 'Forman'},
        {'age': 19, 'email': 'scott_liza@mars.org', 'name': 'Liza', 'position': 'biologist', 'surname': 'Scott'},
        {'age': 17, 'email': 'Saimon_Sc@mars.org', 'name': 'Saymon', 'position': 'middle doctor', 'surname': 'Scott'},
        {'age': 15, 'email': 'scott_sofi@mars.org', 'name': 'Sofi', 'position': 'Passenger', 'surname': 'Scott'},
        {'age': 20, 'email': 'test_user@mars.org', 'name': 'Roman', 'position': 'pilot', 'surname': 'Sulima'}]}
    assert get('http://localhost:5000/api/user').json() == map  # Получение всех записей


def test_get_one_user():
    assert get('http://localhost:5000/api/user/3').json() == {
        'user': {'age': 29, 'email': 'pilot_master_Vil@mars.org', 'name': 'Ridley', 'position': 'pilot',
                 'surname': 'Vilsan'}}
    assert get('http://localhost:5000/api/user/999').json() == {'error': 'Not found'}
    assert get('http://localhost:5000/api/user/"2"').json() == {'error': 'Not found'}


# Тесты на создание записи
def test_create_user():
    assert post('http://localhost:5000/api/user', json={}).json() == {'error': 'Empty request'}
    assert post('http://localhost:5000/api/user', json={'age': 1}).json() == {'error': 'Bad request'}
    assert post('http://localhost:5000/api/user',
                json={'name': 'Roman', 'surname': 'Sulima', 'age': 20, 'position': 'Capitan',
                      'email': 'capitan_roman@gmail.com'}).json() == {'success': 'OK'}


# Тесты на удаление записей
def test_delete_user():
    assert delete('http://localhost:5000/api/user/999').json() == {'error': 'Not found'}
    assert delete('http://localhost:5000/api/user/10').json() == {'success': 'OK'}


# Тесты на изменение данных
def test_update_user():
    assert put('http://localhost:5000/api/user/9', json={'is_finished': True}).json() == {'success': 'OK'}
