import pytest
import numpy as np
from unittest import mock
import os

from test import carregar_imagem_teste, preditar_numero, gerar_numeros_aleatorios

def test_carregar_imagem_teste_valida(tmp_path):
    # Criar imagem dummy
    import cv2
    dummy_image = np.ones((100, 100), dtype=np.uint8) * 255
    img_path = tmp_path / "dummy.png"
    cv2.imwrite(str(img_path), dummy_image)

    img = carregar_imagem_teste(str(img_path))

    assert img.shape == (1, 64, 64, 1)
    assert (img <= 1.0).all()

def test_carregar_imagem_teste_invalida():
    with pytest.raises(FileNotFoundError):
        carregar_imagem_teste("caminho/inexistente.png")

def test_preditar_numero():
    # Mock do model
    mock_model = mock.MagicMock()
    mock_model.predict.return_value = [
        np.eye(10)[[3]],  # milhar: 3
        np.eye(10)[[2]],  # centena: 2
        np.eye(10)[[1]],  # dezena: 1
        np.eye(10)[[4]]   # unidade: 4
    ]

    # Mock da função de carregar imagem
    with mock.patch('test.carregar_imagem_teste', return_value=np.zeros((1, 64, 64, 1))):
        numero = preditar_numero("dummy.png", mock_model)
    
    assert numero == 3214

def test_gerar_numeros_aleatorios():
    with mock.patch('test.salvar_numero_gerado') as mock_salvar:
        gerar_numeros_aleatorios(5)
        assert mock_salvar.call_count == 5
