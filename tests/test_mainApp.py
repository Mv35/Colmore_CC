import sys
sys.path.insert(0, './colmore/')

import pytest
import json
from colmore.main import app as mainApp


@pytest.fixture
def client():
    
    mainApp.config['TESTING'] = True
    with mainApp.test_client() as client:
        yield client


def test_main_route(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_login_route(client):
    rv = client.get('/login')
    assert rv.status_code == 200

def test_authenticate_route(client):
    rv = client.get('/authenticate')
    assert rv.status_code == 405

def test_stats_route(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype,
    }
    data = {
        'search': 'tesla'
    }
    rv = client.post('/stats',data=data,headers=headers)

    assert rv.status_code == 400
