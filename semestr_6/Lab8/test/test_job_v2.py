from requests import post, get, delete, put
import pytest


# Тесты на поиск нужной записи
def test_get_list_jobs():
    defalt_map = {'news': [{'job': 'deployment of residential modules 1 and 2', 'team_leader': 1, 'work_size': 15},
                           {'job': 'deployment of residential modules 3', 'team_leader': 1, 'work_size': 9},
                           {'job': 'Setting up a life support system', 'team_leader': 1, 'work_size': 40},
                           {'job': 'Изучение новых технологий', 'team_leader': 9, 'work_size': 5}]}
    map = get('http://localhost:5000/api/v2/jobs').json()  # Получение всех записей
    assert map == defalt_map


def test_get_one_jobs():
    assert get('http://localhost:5000/api/v2/jobs/3').json() == {
        'jobs': {'job': 'Setting up a life support system', 'team_leader': 1, 'work_size': 40}}
    assert get('http://localhost:5000/api/v2/jobs/999').json() == {'message': 'Jobs 999 not found'}
    assert get('http://localhost:5000/api/v2/jobs/"2"').json() == {'error': 'Not found'}


def test_create_jobs():
    assert post('http://localhost:5000/api/v2/jobs', json={}).json() == {
        'message': {'job': 'Missing required parameter in the JSON body or the post body or the query string'}}
    assert post('http://localhost:5000/api/v2/jobs',
                json={'team_leader': 1}).json() == {
               'message': {'job': 'Missing required parameter in the JSON body or the post body or the query string'}}
    assert post('http://localhost:5000/api/v2/jobs',
                json={'team_leader': 1,
                      'job': "Test_string",
                      'work_size': 2}).json() == {'success': 'OK'}


def test_update_jobs():
    assert put('http://localhost:5000/api/v2/jobs/5', json={'team_leader': 2}).json() == {'success': 'OK'}


# Тесты на удаление записей
def test_delete_jobs():
    assert delete('http://localhost:5000/api/v2/jobs/999').json() == {'message': 'Jobs 999 not found'}
    assert delete('http://localhost:5000/api/v2/jobs/5').json() == {'success': 'OK'}
