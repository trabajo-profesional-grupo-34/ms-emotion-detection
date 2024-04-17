from fastapi import FastAPI
from deepface import DeepFace
from pydantic import BaseModel
import base64


class Image(BaseModel):
    base64_str: str

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "It's alive!"}


@app.get("/hello/{name}")
def hello_name(name: str = "World"):
    return {"message": f"Hello, {name}!"}


@app.get("/emotion")
def test():
    with open('./images/happy_face.jpg', 'rb') as file:
        image_data = file.read()
        base64_encoded_image = base64.b64encode(image_data)
        base64_string = base64_encoded_image.decode('utf-8')

        return {
            "emotion": DeepFace.analyze(
                img_path = f"data:image/jpeg;base64,{base64_string}", 
                actions = ['emotion']
            )[0]["dominant_emotion"]
        }


@app.post("/dominant_emotion", status_code=200)
def get_dominant_emotion(image: Image):
    dominant_emotion = DeepFace.analyze(
        img_path = image.base64_str, 
        actions = ['emotion']
    )[0]["dominant_emotion"]

    return { "dominant_emotion": dominant_emotion }
