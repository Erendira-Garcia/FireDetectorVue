# main.py
from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from preprocessing import preprocessing_image
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
# from flask import jsonify

#Origenes permitidos para CORS
origins = [
"http://localhost:8000",
"http://localhost:5500",
"http://localhost:5502",
"http://127.0.0.1:8000",
"http://127.0.0.1:5500",
"http://127.0.0.1:5502"
]

app = FastAPI()

# Cargar el modelo
model = load_model('model.h5')

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    """
    Endpoint para predecir si una imagen contiene un incendio.

    Parámetros:
    - file: archivo de imagen a ser procesado

    Retorna:
    - Un diccionario con la clave "Incendio" y el valor booleano que indica si se detectó un incendio en la imagen.
    - En caso de error al procesar la imagen, retorna un diccionario con la clave "error" y un mensaje de error.
    """

    contents = await file.read()
    image_path = "temp_image.jpg"

    with open(image_path, "wb") as f:
        f.write(contents)

    img = preprocessing_image(image_path)
    if img is None:
        return {"error": "Error al procesar la imagen"}

    img_array = np.expand_dims(img, axis=0)
    prediction = model.predict(img_array)
    is_fire = prediction[0][0] >= 0.5

    return {"is_fire": bool(is_fire)}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite todos los origenes
    allow_credentials=True,
    allow_methods=["\*"],
    allow_headers=["\*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)