# --- Importar as bibliotecas --- #
import requests
from json import dumps


def adicionar_receita(**kwargs) -> None:
    """
    Função responsável por adicionar a receita ao banco de dados.
    :param kwargs: Tipo da receita, nome, ingredientes e modo de preparo.
    """
    # --- Obter as entradas da função --- #
    banco = kwargs['banco']
    nome_receita = kwargs['nome_receita']
    ingredientes = kwargs['ingredientes']
    modo_preparo = kwargs['modo_preparo']

    # --- Link do banco de dados --- #
    link = 'https://wikireceitas-aace2-default-rtdb.firebaseio.com/'

    # --- Criar o dicionário para adicionar os dados ao banco --- #
    dic_receita = {
        nome_receita: {
            'ingredientes': ingredientes,
            'modo_preparo': modo_preparo
        }
    }

    # --- Enviar ao banco de dados a receita --- #
    requests.patch(f'{link}/{banco}/.json', data=dumps(dic_receita))
