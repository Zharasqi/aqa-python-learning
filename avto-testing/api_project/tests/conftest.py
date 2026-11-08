import pytest
from api_project.config import BASE_URL
from api_project.config import TIMEOUT
from api_project.test_data.post_payloads import payload_post
from api_project.test_data.post_payloads import payload_post_patch
from api_project.test_data.post_payloads import payload_post_put

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def timeout():
    return TIMEOUT

@pytest.fixture
def payload():
    return payload_post.copy()

@pytest.fixture
def post_id():
    return 1

@pytest.fixture
def invalid_post_id():
    return 9999

@pytest.fixture
def updated_post_payload():
    return payload_post_patch.copy()

@pytest.fixture
def put_updated_post_payload():
    return payload_post_put.copy()