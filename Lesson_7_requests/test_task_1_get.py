import requests
import pytest
from pydantic import BaseModel, ValidationError

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

@pytest.fixture
def post_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    return response.json()

user_data = {
    "userId": 1,
    "id": 1,
    "body": "Zharas"}

def test_post_without_title():
    with pytest.raises(ValidationError) as e:
        Post.model_validate(user_data)
    first_error = e.value.errors()[0]
    assert first_error['loc'] == ('title',)
    assert first_error['type'] == 'missing'

def test_model_validation(post_data):
    data_validation = Post.model_validate(post_data)
    assert data_validation.id == 1

def test_get_post(post_data):
    assert isinstance(post_data, dict)
    assert post_data['id'] == 1
    assert 'userId' in post_data
    assert 'id' in post_data
    assert 'title' in post_data
    assert 'body' in post_data
    assert isinstance(post_data['title'], str)
    assert post_data['title']

def test_get_invalid_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1000')
    assert response.status_code == 404