# 🔢 Reconhecimento de Números Cistercienses

Este é um projeto que gera, exibe e reconhece números Cistercienses utilizando Python, OpenCV, TensorFlow e uma interface Tkinter.

## 📦 Funcionalidades

- Gera imagens de números no sistema numeral Cisterciense
- Salva as imagens automaticamente em uma pasta organizada
- Treina um modelo de rede neural convolucional (CNN) para reconhecer os números (opcional)
- Faz predição a partir de uma imagem usando modelo multi-saída (milhar, centena, dezena, unidade)
- Interface gráfica simples com Tkinter para gerar ou carregar uma imagem e reconhecer o número

## 📁 Estrutura do Projeto

```
NumerosCistercienses/
├── generateNumber.py             # Gera e desenha números Cistercienses com OpenCV
├── neural.py                     # Treinamento da rede neural com saída multi-componentes (opcional)
├── index.py                      # Execução por linha de comando (CLI)
├── cistercian_gui_app.py         # Interface gráfica Tkinter
├── modelo_cistercian_multioutput.h5  # Modelo treinado salvo
├── output/imagens_geradas/      # Pasta com as imagens geradas automaticamente
```

## 🚀 Como executar

### Instalar dependências
```bash
pip install tensorflow numpy opencv-python pillow
```

### Treinar o modelo (opcional se já tiver o .h5)
```bash
python neural.py
```

### Executar via interface gráfica
```bash
python cistercian_gui_app.py
```

## 🧠 Sobre o modelo

A rede neural foi projetada para identificar cada componente do número (milhar, centena, dezena e unidade) separadamente com saídas independentes (`multioutput`).

> O arquivo `modelo_cistercian_multioutput.h5` já está incluso no projeto. O treinamento é opcional.

## 📸 Exemplo

Ao inserir o número `4723`, o sistema gera a imagem correspondente ao seu formato Cisterciense, a exibe e depois essa imagem salva na pasta `img` pode ser usada para testar o modelo.

---

## 🛠️ Feito com:
- Python
- OpenCV
- TensorFlow / Keras
- Pillow
- Tkinter

---

Se você quiser contribuir com melhorias ou ideias, fique à vontade para abrir um PR ou issue 😄
