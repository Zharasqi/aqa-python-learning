import requests
from pydantic import BaseModel

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

def test_list_validate():
    response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=10)
    assert response.status_code == 200
    raw_list = response.json()
    assert isinstance(raw_list, list)
    validated_post = []
    for post_data in raw_list:
        valid_data = Post.model_validate(post_data)
        validated_post.append(valid_data)
    assert len(validated_post) == len(raw_list)
    assert isinstance(validated_post[0], Post)
    assert validated_post[0].id == 1


def test_get_post_list():
    response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=10)
    assert response.status_code == 200
    post_list = response.json()
    assert isinstance(post_list, list)
    assert len(post_list) == 100
    assert isinstance(post_list[0], dict)
    assert post_list[0]['id'] == 1

