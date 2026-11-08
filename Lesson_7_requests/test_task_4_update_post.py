import requests

payload = {
    'id': 1,
    'userId': 212,
    'title': 'New Title',
    'body': 'New Content'
}
def test_update_post():
    response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=payload, timeout=10)
    assert response.status_code == 200
    response_post = response.json()
    assert isinstance(response_post, dict)
    assert response_post['title'] == payload['title']
    assert response_post['body'] == payload['body']
    assert response_post['userId'] == payload['userId']
    assert response_post['id'] == payload['id']

payload_patch = {
    'title': 'Update Title',
}

def test_patch_post():
    response = requests.patch('https://jsonplaceholder.typicode.com/posts/1', json=payload_patch, timeout=10)
    assert response.status_code == 200
    response_post = response.json()
    assert isinstance(response_post, dict)
    assert response_post['title'] == payload_patch['title']
    assert response_post['id'] == 1

def test_delete_post():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1', timeout=10)
    assert response.status_code == 200
    response_post = response.json()
    assert response_post == {}