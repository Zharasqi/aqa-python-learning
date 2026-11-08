import requests
import pytest

@pytest.mark.parametrize('user_id', [1, 2, 3])
def test_get_posts_by_user(user_id):
    query_params = {"userId": user_id}
    response = requests.get('https://jsonplaceholder.typicode.com/posts', params=query_params, timeout=10)
    assert response.status_code == 200
    response_headers = response.headers
    assert "application/json" in response_headers['content-type']
    response_json = response.json()
    assert isinstance(response_json, list)
    assert response_json
    for post in response_json:
        assert post['userId'] == user_id
