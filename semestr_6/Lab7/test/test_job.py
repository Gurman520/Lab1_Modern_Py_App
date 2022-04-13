from requests import post, get, delete, put
import pytest


# Тесты на поиск нужной записи
def test_get_jobs():
    defalt_map = {'jobs': [{'job': 'deployment of residential modules 1 and 2', 'team_leader': 1, 'work_size': 15},
                           {'job': 'deployment of residential modules 3', 'team_leader': 1, 'work_size': 9},
                           {'job': 'Setting up a life support system', 'team_leader': 1, 'work_size': 40},
                           {'job': 'Изучение новых технологий', 'team_leader': 9, 'work_size': 5}]}
    map = get('http://localhost:5000/api/jobs').json()  # Получение всех записей
    assert map == defalt_map


def test_get_one_jobs():
    assert get('http://localhost:5000/api/jobs/3').json() == {
        'jobs': {'id': 3, 'job': 'Setting up a life support system', 'team_leader': 1, 'work_size': 40}}
    assert get('http://localhost:5000/api/jobs/999').json() == {'error': 'Not found'}
    assert get('http://localhost:5000/api/jobs/"2"').json() == {'error': 'Not found'}


# # Тесты на создание записи
def test_create_jobs():
    assert post('http://localhost:5000/api/jobs', json={}).json() == {'error': 'Empty request'}
    assert post('http://localhost:5000/api/jobs',
                json={'team_leader': 1}).json() == {'error': 'Bad request'}
    assert post('http://localhost:5000/api/jobs',
                json={'team_leader': 1,
                      'job': "Test_string",
                      'work_size': 2,
                      'is_finished': False}).json() == {'success': 'OK'}


# Тесты на удаление записей
def test_delete_jobs():
    assert delete('http://localhost:5000/api/jobs/999').json() == {'error': 'Not found'}
    assert delete('http://localhost:5000/api/jobs/5').json() == {'success': 'OK'}


# Тесты на изменение данных
def test_update_jobs():
    assert put('http://localhost:5000/api/jobs/4', json={'is_finished': True}).json() == {'success': 'OK'}
