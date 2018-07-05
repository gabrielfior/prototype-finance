from apistar import test
from app import app

client = test.TestClient(app)

def test_welcome():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() ==  {'hello': 'world'}

def test_data_fetcher():
    response = client.get('/data')
    assert response.status_code == 200

    # Delivered json must be an array to be plotted later, since it must contain a list of series
    assert isinstance(response.json(), list)
