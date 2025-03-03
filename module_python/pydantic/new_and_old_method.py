from pydantic import BaseModel

class User(BaseModel):
    uuid: str
    name: str

data = """{"uuid": "dickbutt",
        "name": "Gill Bates"}"""


"""User.parse_raw(data)     ->      User.model_validate_json(data)"""

@validator      ->