from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True

assert User.model_fields["id"].is_required()
assert not User.model_fields["is_active"].is_required()
assert User.model_fields["is_active"].default is True
assert User.model_fields["name"].annotation is str