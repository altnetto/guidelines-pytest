"""
Esse é o primeiro local onde serão buscadas informações acerca dos testes usando o pytest

Aqui, devemos inserir fixtures, que são decorators para acionar recursos do nosso app e o próprio app
"""
import pytest
from meuapp.app import create_app
"""
A fixture é declarada com ou sem a keyword 'scope', entretanto, é convencionado o uso de 'module' para
trabalhar com módulos e 'function' para trabalhar com funções isoladas.


*** Você deve sempre rodar o pytest dentro do diretório do PROJETO, nesse caso, ~./meuapp

Para rodar os testes, basta efetuar:

> pytest tests/ -v

o item -v serve para tornar a saída verbosa, ou seja, para explicar o que está sendo testado de forma mais detalhada
"""
@pytest.fixture(scope="module")
def app():
    return create_app()