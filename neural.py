import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models, Input
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping

# 1. Função para carregar imagens e extrair milhar, centena, dezena e unidade
def carregar_dados_componentes(img_folder, img_size=(64, 64)):
    imagens, milhares, centenas, dezenas, unidades = [], [], [], [], []

    for filename in os.listdir(img_folder):
        if filename.endswith(".png"):
            path = os.path.join(img_folder, filename)
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, img_size)
            img = img / 255.0
            imagens.append(img)

            numero = int(filename.split("number")[1].split(".png")[0])
            milhares.append((numero // 1000) % 10)
            centenas.append((numero // 100) % 10)
            dezenas.append((numero // 10) % 10)
            unidades.append(numero % 10)

    imagens = np.array(imagens)
    imagens = np.expand_dims(imagens, axis=-1)  # (N, 64, 64, 1)

    return imagens, np.array(milhares), np.array(centenas), np.array(dezenas), np.array(unidades)

# 2. Carregando dados da pasta 'img'
X, Y_m, Y_c, Y_d, Y_u = carregar_dados_componentes("./img")

# 3. Split e one-hot
X_train, X_test, Ym_train, Ym_test = train_test_split(X, Y_m, test_size=0.2, random_state=42)
_, _, Yc_train, Yc_test = train_test_split(X, Y_c, test_size=0.2, random_state=42)
_, _, Yd_train, Yd_test = train_test_split(X, Y_d, test_size=0.2, random_state=42)
_, _, Yu_train, Yu_test = train_test_split(X, Y_u, test_size=0.2, random_state=42)

Ym_train = to_categorical(Ym_train, 10)
Yc_train = to_categorical(Yc_train, 10)
Yd_train = to_categorical(Yd_train, 10)
Yu_train = to_categorical(Yu_train, 10)

Ym_test = to_categorical(Ym_test, 10)
Yc_test = to_categorical(Yc_test, 10)
Yd_test = to_categorical(Yd_test, 10)
Yu_test = to_categorical(Yu_test, 10)

# 4. Arquitetura do modelo com 4 saídas
input_img = Input(shape=(64, 64, 1))
x = layers.Conv2D(32, (3, 3), activation="relu")(input_img)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Conv2D(64, (3, 3), activation="relu")(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Conv2D(64, (3, 3), activation="relu")(x)
x = layers.Flatten()(x)
x = layers.Dense(128, activation="relu")(x)

# Saídas
out_m = layers.Dense(10, activation="softmax", name="milhar")(x)
out_c = layers.Dense(10, activation="softmax", name="centena")(x)
out_d = layers.Dense(10, activation="softmax", name="dezena")(x)
out_u = layers.Dense(10, activation="softmax", name="unidade")(x)

model = models.Model(inputs=input_img, outputs=[out_m, out_c, out_d, out_u])

# 5. Compilar e treinar
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics={
        "milhar": "accuracy",
        "centena": "accuracy",
        "dezena": "accuracy",
        "unidade": "accuracy"
    }
)
early = EarlyStopping(patience=5, restore_best_weights=True)

model.fit(
    X_train,
    {"milhar": Ym_train, "centena": Yc_train, "dezena": Yd_train, "unidade": Yu_train},
    epochs=30,
    batch_size=32,
    validation_data=(X_test, {"milhar": Ym_test, "centena": Yc_test, "dezena": Yd_test, "unidade": Yu_test}),
    callbacks=[early]
)

# 6. Avaliação
resultados = model.evaluate(X_test, {
    "milhar": Ym_test,
    "centena": Yc_test,
    "dezena": Yd_test,
    "unidade": Yu_test
})

acc_m, acc_c, acc_d, acc_u = resultados[5], resultados[6], resultados[7], resultados[8]

print(f"\nAcurácia por componente:")
print(f"  Milhar:  {acc_m:.2%}")
print(f"  Centena: {acc_c:.2%}")
print(f"  Dezena:  {acc_d:.2%}")
print(f"  Unidade: {acc_u:.2%}")

# 7. Salvar o modelo
model.save("modelo_treinado.h5")