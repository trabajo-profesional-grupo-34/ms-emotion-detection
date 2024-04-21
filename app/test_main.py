from fastapi.testclient import TestClient
from .main import app
import base64


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "It's alive!"}


def test_hello_name_with_world():
    response = client.get("/hello/World")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_hello_name_with_alex():
    response = client.get("/hello/Alex")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Alex!"}


def test():
    response = client.get("/emotion")
    assert response.status_code == 200
    assert response.json() == {"emotion": "happy"}


def test_get_dominant_emotion():
    with open('./images/happy_face.jpg', 'rb') as file:
        image_data = file.read()

    base64_encoded_image = base64.b64encode(image_data)
    base64_str = base64_encoded_image.decode('utf-8')

    response = client.post("/dominant_emotion", json={
        "base64_str": f"data:image/jpeg;base64,{base64_str}"
    })

    assert response.status_code == 200
    assert response.json() == {"dominant_emotion": "happy"}
