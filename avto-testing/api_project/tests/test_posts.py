import allure
import pytest
import requests
from api_project.models.post import Post
from api_project.clients.posts_client import get_post
from api_project.clients.posts_client import create_post
from api_project.clients.posts_client import update_post
from api_project.clients.posts_client import delete_post
from api_project.clients.posts_client import update_post_put
from api_project.factories.post_factory import make_post_payload

@allure.feature("Posts API")
@allure.story("Получение поста")
@allure.title("Проверка присутствия application/json")
@pytest.mark.smoke
@pytest.mark.api
def test_get_first_post(base_url, timeout, post_id):
    with allure.step(f"1 Шаг. отправка запроса в {base_url}"):
        response = get_post(base_url, timeout, post_id)
        allure.attach(
            response.text,
            name = "Получение тело ответа",
            attachment_type = allure.attachment_type.JSON)
    with allure.step("2 Шаг. Проверка что статус код равен 200"):
        assert response.status_code == 200
    response_json = response.json()
    validated_data = Post.model_validate(response_json)
    with allure.step("3 Шаг. Проверка заголовка Content-Type"):
        assert "application/json" in response.headers["Content-Type"]
    assert validated_data.id == 1

@pytest.mark.smoke
def test_create_new_post(base_url, timeout, payload):
    response = create_post(base_url, timeout, payload)
    assert response.status_code == 201
    response_json = response.json()
    validated_post = Post.model_validate(response_json)
    assert validated_post.userId == payload['userId']
    assert validated_post.title == payload['title']
    assert validated_post.body == payload['body']

@allure.feature("Posts API")
@allure.story("Получение поста")
@allure.title("Проверка несушествующего post")
def test_get_nonexistent_post_returns_404(base_url, timeout, invalid_post_id):
    response = get_post(base_url, timeout, invalid_post_id)
    assert response.status_code == 404
    with pytest.raises(requests.HTTPError):
        response.raise_for_status()
    response_json = response.json()
    assert response_json == {}

@pytest.mark.smoke
def test_update_first_post(base_url, timeout, post_id, updated_post_payload):
    response = update_post(base_url, timeout, post_id, updated_post_payload)
    assert response.status_code == 200
    response_json = response.json()
    validated_post = Post.model_validate(response_json)
    assert validated_post.id == post_id
    assert validated_post.title == updated_post_payload['title']

def test_delete_post(base_url, timeout, post_id):
    response = delete_post(base_url, timeout, post_id)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json == {}

@pytest.mark.parametrize(
    "get_id",[1,2,3],
    ids = ["post_id=1", "post_id=2", "post_id=3"]
)
@allure.feature("Posts API")
@allure.story("Получение поста")
@allure.title("Проверка поста по соответствию готовой модели Post")
def test_get_post_by_id(base_url, timeout, get_id):
    response = get_post(base_url, timeout, get_id)
    assert response.status_code == 200
    response_json = response.json()
    validated_post = Post.model_validate(response_json)
    assert validated_post.id == get_id

@allure.feature("Posts API")
@allure.story("Получение поста")
@allure.title("Проверка ожидаемой ошибки по таймауту")
def test_get_post_timeout(base_url, timeout, post_id):
    with allure.step("1 Шаг. Отправляется GET запрос с минимальным временем ожидания"):
        with pytest.raises(requests.exceptions.Timeout) as exc_info:
            get_post(base_url, 0.001, post_id)
        allure.attach(
                str(exc_info.value),
                name = "Ошибка таймаут",
                attachment_type = allure.attachment_type.TEXT)
def test_get_post_connection_error(timeout, post_id):
    with pytest.raises(requests.exceptions.ConnectionError):
        get_post("http://127.0.0.1:1", timeout, post_id)

def test_get_post_headers(base_url, timeout, post_id):
    headers = {"Accept": "application/json"}
    response = get_post(base_url, timeout, post_id, headers=headers)
    assert response.status_code == 200
    assert response.request.headers['Accept'] == 'application/json'

@allure.feature("Posts API")
@allure.story("Получение поста")
@allure.title("Проверка присутствия параметра Authorization")
def test_get_post_auth_token(base_url, timeout, post_id):
    headers = {
        "Authorization": "Bearer test-token"
    }
    response = get_post(base_url, timeout, post_id, headers=headers)
    assert response.status_code == 200
    with allure.step("Проверка заголовка Authorization"):
        assert response.request.headers['Authorization'] == 'Bearer test-token'

@allure.feature("Posts API")
@allure.story("Получение поста")
@allure.title("Проверка корректной передачи auth параметров")
def test_get_post_login(base_url, timeout, post_id):
    auth = ('test-user', 'test-password')
    response = get_post(base_url, timeout, post_id, auth=auth)
    assert response.status_code == 200
    assert response.request.headers["Authorization"].startswith("Basic ")

def test_update_put_post(base_url, timeout, post_id, put_updated_post_payload):
    response = update_post_put(base_url, timeout, post_id, put_updated_post_payload)
    assert response.status_code == 200
    response_json = response.json()
    validated_put_post = Post.model_validate(response_json)
    assert validated_put_post.id == post_id
    assert validated_put_post.userId == put_updated_post_payload['userId']
    assert validated_put_post.title == put_updated_post_payload['title']
    assert validated_put_post.body == put_updated_post_payload['body']

def test_factory_payload():
    payload = make_post_payload()
    assert payload['userId'] == 1
    assert payload['title'] == "new title for mini-app"
    assert payload['body'] == "new body for mini-app"

def test_factory_new_title():
    payload = make_post_payload(title="update current title for mini-app")
    assert payload['title'] == "update current title for mini-app"
    assert payload['body'] == "new body for mini-app"
    assert payload['userId'] == 1

def test_factory_finally_check():
    add_new_title = make_post_payload()
    current_title = make_post_payload()
    add_new_title['title'] = "finally title for mini-app"
    assert add_new_title is not current_title
    assert add_new_title['title'] == "finally title for mini-app"
    assert add_new_title['body'] == current_title['body']
    assert add_new_title['userId'] == current_title['userId']

def test_create_post_with_factory_payload(base_url, timeout):
    payload = make_post_payload(title="update current title for mini-app")
    response = create_post(base_url, timeout, payload)
    assert response.status_code == 201
    response_json = response.json()
    validated_post = Post.model_validate(response_json)
    assert validated_post.title == payload['title']
    assert validated_post.body == payload['body']
    assert validated_post.userId == payload['userId']
