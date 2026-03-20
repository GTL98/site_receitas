# --- Importar as bibliotecas --- #
import requests
from json import dumps


def atualizar_receita(**kwargs) -> None:
    """
    Função responsávle por atualizar a receita desejada.
    :param kwargs:
    :return:
    """
    # --- Obter as entradas da função --- #
    banco = kwargs['banco']
    nome_receita = kwargs['nome_receita']
    ingredientes = kwargs['ingredientes']
    modo_preparo = kwargs['modo_preparo']

    # --- Link do banco de dados --- #
    link = 'https://wikireceitas-aace2-default-rtdb.firebaseio.com/'

    # --- Obter o dicionário atual da receita --- #
    dic_requisicao = requests.get(f'{link}/{banco}/{nome_receita}/.json').json()
    dic_copia = dic_requisicao

    # --- Atualizar as informações --- #
    dic_copia['ingredientes'] = ingredientes
    dic_copia['modo_preparo'] = modo_preparo

    # --- Atualizar a receita --- #
    requests.patch(f'{link}/{banco}/{nome_receita}/.json', data=dumps(dic_copia))