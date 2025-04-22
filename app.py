import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import os
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from generateNumber import mostrar_numero_gerado

# Função para carregar imagem e preprocessar
def carregar_imagem_para_predicao(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (64, 64)) / 255.0
    img = np.expand_dims(img, axis=-1)
    img = np.expand_dims(img, axis=0)
    return img

# Predição com modelo multi-saída
def preditar_numero(path_img):
    img = carregar_imagem_para_predicao(path_img)
    pred_m, pred_c, pred_d, pred_u = model.predict(img)
    return np.argmax(pred_m)*1000 + np.argmax(pred_c)*100 + np.argmax(pred_d)*10 + np.argmax(pred_u)

# Gerar imagem com OpenCV e preditar
def gerar():
    try:
        numero = int(entry_num.get())
        if not (1 <= numero <= 9999):
            raise ValueError
        mostrar_numero_gerado(numero)
        path_img = f"img/number{numero}.png"
        atualizar_imagem(path_img)
    except ValueError:
        messagebox.showerror("Erro", "Insira um número entre 1 e 9999")

# Carregar imagem manualmente e preditar
def carregar_e_predizer():
    path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if path:
        numero_predito = preditar_numero(path)
        atualizar_imagem(path)
        resultado_var.set(f"Predito: {numero_predito}")

# Atualizar imagem exibida na tela
def atualizar_imagem(path):
    img = Image.open(path).resize((128, 128))
    img_tk = ImageTk.PhotoImage(img)
    canvas.itemconfig(canvas_img, image=img_tk)
    canvas.image = img_tk

# Carregar modelo treinado
model = load_model("modelo_treinado.h5")

# Criar janela principal
root = tk.Tk()
root.title("Reconhecimento de Números Cistercienses")
root.geometry("400x400")

# Entrada para gerar número
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)
tk.Label(entry_frame, text="Digite um número (1 a 9999):").pack(side="left")
entry_num = tk.Entry(entry_frame, width=8)
entry_num.pack(side="left")

# Botões
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Gerar", command=gerar).pack(side="left", padx=5)
tk.Button(btn_frame, text="Carregar imagem", command=carregar_e_predizer).pack(side="left", padx=5)

# Canvas para imagem
canvas = tk.Canvas(root, width=128, height=128)
canvas.pack(pady=10)
canvas_img = canvas.create_image(0, 0, anchor="nw")

# Resultado
resultado_var = tk.StringVar()
tk.Label(root, textvariable=resultado_var, font=("Arial", 14)).pack(pady=10)

# Iniciar app
root.mainloop()
