from requests import post, get, delete, put
import pytest


# Тесты на поиск нужной записи
def test_get_user():
    map = {'news': [{'age': 21, 'name': 'Ridley', 'surname': 'Scott'}, {'age': 25, 'name': 'Omar', 'surname': 'Eps'},
                    {'age': 29, 'name': 'Ridley', 'surname': 'Vilsan'}, {'age': 40, 'name': 'Greg', 'surname': 'House'},
                    {'age': 24, 'name': 'Eric', 'surname': 'Forman'}, {'age': 19, 'name': 'Liza', 'surname': 'Scott'},
                    {'age': 17, 'name': 'Saymon', 'surname': 'Scott'}, {'age': 15, 'name': 'Sofi', 'surname': 'Scott'},
                    {'age': 20, 'name': 'Roman', 'surname': 'Sulima'}]}
    assert get('http://localhost:5000/api/v2/users').json() == map  # Получение всех записей


def test_get_one_user():
    assert get('http://localhost:5000/api/v2/users/3').json() == {
        'Users': {'age': 29, 'name': 'Ridley', 'surname': 'Vilsan'}}
    assert get('http://localhost:5000/api/v2/users/999').json() == {'message': 'Users 999 not found'}
    assert get('http://localhost:5000/api/v2/users/"2"').json() == {'error': 'Not found'}


# Тесты на создание записи
def test_create_user():
    assert post('http://localhost:5000/api/v2/users', json={}).json() == {
        'message': {'name': 'Missing required parameter in the JSON body or the post body or the query string'}}
    assert post('http://localhost:5000/api/v2/users', json={'age': 1}).json() == {
        'message': {'name': 'Missing required parameter in the JSON body or the post body or the query string'}}
    assert post('http://localhost:5000/api/v2/users',
                json={'name': 'Roman', 'surname': 'Sulima', 'age': 20}).json() == {'success': 'OK'}


def test_update_user():
    assert put('http://localhost:5000/api/v2/users/10', json={'age': 21}).json() == {'success': 'OK'}


# Тесты на удаление записей
def test_delete_user():
    assert delete('http://localhost:5000/api/v2/users/999').json() == {'message': 'Users 999 not found'}
    assert delete('http://localhost:5000/api/v2/users/10').json() == {'success': 'OK'}
