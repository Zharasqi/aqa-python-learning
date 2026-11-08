import requests
import logging
logger = logging.getLogger(__name__)

def get_post(base_url, timeout, post_id, headers=None, auth=None):
    logger.info(f"GET {base_url}/posts/{post_id}")
    try:
        response = requests.get(f'{base_url}/posts/{post_id}', timeout=timeout, headers=headers, auth=auth)
        logger.info(f'Статус код равен:{response.status_code}')
        return response
    except requests.exceptions.Timeout:
        logger.error(f'GET {base_url}/posts/{post_id} timeout')
        raise
    except requests.exceptions.ConnectionError:
        logger.error(f'GET {base_url}/posts/{post_id} connection error')
        raise

def create_post(base_url, timeout, payload):
    logger.info(f'POST {base_url}/posts')
    response = requests.post(f'{base_url}/posts', json=payload, timeout=timeout)
    logger.info(f'Статус код равен:{response.status_code}')
    return response

def update_post(base_url, timeout, post_id, payload):
    logger.info(f'PATCH {base_url}/posts/{post_id}')
    response = requests.patch(f'{base_url}/posts/{post_id}', json=payload, timeout=timeout)
    logger.info(f'Статус код равен: {response.status_code}')
    return response

def delete_post(base_url, timeout, post_id):
    logger.info(f'DELETE {base_url}/posts/{post_id}')
    response = requests.delete(f'{base_url}/posts/{post_id}', timeout=timeout)
    logger.info(f'Статус код равен: {response.status_code}')
    return response

def update_post_put(base_url, timeout, post_id, payload):
    logger.info(f'PUT {base_url}/posts/{post_id}')
    response = requests.put(f'{base_url}/posts/{post_id}', json=payload, timeout=timeout)
    logger.info(f'Статус код равен: {response.status_code}')
    return response