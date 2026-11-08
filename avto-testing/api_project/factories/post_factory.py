def make_post_payload(userId=1, title="new title for mini-app", body="new body for mini-app"):
    payload_post_option = {
        "userId": userId,
        "title": title,
        "body": body,
    }
    return payload_post_option