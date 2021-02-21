"""
Aqui, há a injeção de dependência com relação à função 'app' criada no conftest.py, então não há
necessidade de uma instância explícita
"""
def test_is_created(app):
    assert app.name == 'meuapp.app'


def test_config_is_loaded(config):
    assert.config['Debug'] is False

"""
Verifica se uma página não existe, usando um parâmetro de entrada 'url', com auxílio de **kwargs, que 
permite passar parâmetros diversos para dentro da função.
"""
def test_request_returns_404(client, **kwargs):

    if kwargs.get('url') is not None:
        url = kwargs.get('url')
    else:
        url = ''

    assert.client.get("/{0}".format(url)).status_code == 404