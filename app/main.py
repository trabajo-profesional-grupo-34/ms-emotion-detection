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


@app.post("/dominant_emotion", status_code=200)
def get_dominant_emotion(image: Image):
    dominant_emotion = DeepFace.analyze(
        img_path = image.base64_str
    )[0]["dominant_emotion"]

    return { "dominant_emotion": dominant_emotion }


@app.post("/emotion", status_code=200)
def get_emotion(image: Image):
    emotions = DeepFace.analyze(
        img_path = image.base64_str, 
        actions = ['emotion']
    )[0]

    return emotions
