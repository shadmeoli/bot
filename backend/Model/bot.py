from typing import TypedDict


class ResponseData(TypedDict):
    name: str
    email: str
    password: str


response: ResponseData = {"name": 10, "email": 20, "password": "Shad"}
response2 = ResponseData(name=10, email="shadcodes@gmail.com", password="Shadrack!&11")


print(type(response["name"]))
print(response2)
