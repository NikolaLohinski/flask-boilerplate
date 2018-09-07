# -*- coding: utf-8 -*-
"""
Basic unit testing of API

@author: NikolaLohinski (https://github.com/NikolaLohinski)
@date: 02/02/09
"""


def test_get_empty_inventions(client):
    """After basic creation of DB test if get inventions is empty list"""
    request = client.get('api/v0/inventions')
    assert request.status_code == 200
    body = request.json  # gives you a list
    assert body['success']
    assert isinstance(body['result']['inventions'], list)
    assert len(body['result']['inventions']) == 0


def test_re_init_db(client):
    """Test if re init of DB yields 17 records from inventions.json file"""
    request = client.put('api/v0/inventions/init')
    assert request.status_code == 200
    body = request.json
    assert body['success']
    assert isinstance(body['result']['inventions'], list)
    assert len(body['result']['inventions']) == 17


def test_add_invention(client):
    """Test adding an invention to DB"""
    invention = {
        'name': 'test invention',
        'date': 1564
    }
    request = client.post('api/v0/inventions', json=invention)
    assert request.status_code == 200
    body = request.json
    assert body['success']
    record = body['result']['invention']
    assert all(record[key] == value
               for key, value in invention.items())
    # Test if everything was added
    request = client.get('api/v0/inventions')
    body = request.json
    assert body['result']['inventions'][0] == record


def test_delete_invention(client):
    """Test deleting an invention from DB"""
    invention = {
        'name': 'new invention',
        'date': 1798
    }
    request = client.post('api/v0/inventions', json=invention)
    assert request.status_code == 200
    body = request.json
    assert body['success']
    _id = body['result']['invention']['_id']
    request = client.delete('api/v0/inventions/%s' % _id)
    assert request.status_code == 200
    record = request.json['result']['invention']
    request = client.get('api/v0/inventions')
    body = request.json
    assert record not in body['result']['inventions']
