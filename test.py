import cv2
import numpy as np
from tensorflow.keras.models import load_model
from generateNumber import salvar_numero_gerado 
import os

def carregar_imagem_teste(caminho_imagem):
    img = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (64, 64))
    img = img / 255.0
    img = np.expand_dims(img, axis=-1)
    img = np.expand_dims(img, axis=0)
    return img

def preditar_numero(caminho_imagem, model):
    img = carregar_imagem_teste(caminho_imagem)
    pred_m, pred_c, pred_d, pred_u = model.predict(img)
    return np.argmax(pred_m)*1000 + np.argmax(pred_c)*100 + np.argmax(pred_d)*10 + np.argmax(pred_u)

# Carregar modelo
model = load_model("modelo_treinado.h5")

# Preciso gerar 1000 numeros aleatórios
def gerar_numeros_aleatorios(num):
    for i in range(num):
        numero = np.random.randint(1, 9999)
        salvar_numero_gerado(numero)

gerar_numeros_aleatorios(1000)


