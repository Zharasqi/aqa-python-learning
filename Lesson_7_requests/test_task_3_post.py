import requests

payload = {
    "userId": 1,
    "title": "New_first_post",
    "body": "This is my first post"
}

def test_create_post():
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload, timeout=10)
    assert response.status_code == 201
    response_post = response.json()
    assert isinstance(response_post, dict)
    assert response_post['title'] == payload['title']
    assert response_post['body'] == payload['body']
    assert response_post['userId'] == payload['userId']
    assert  'id' in response_post
    assert isinstance(response_post['id'], int)

