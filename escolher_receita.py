# --- Importar o requests --- #
import requests


def escolher_receita(banco: str) -> list:
    """
    Função responsável por selecionar o banco de dados com as receitas.
    :param banco: Banco da receita selecionada ('doce', 'salgado', 'paes')
    :return: Chaves como o nome das receitas.
    """
    # --- Link do banco de dados --- #
    link = 'https://wikireceitas-aace2-default-rtdb.firebaseio.com/'

    # --- Obter as receitas --- #
    dic_requisicao = requests.get(f'{link}/{banco}/.json')

    return dic_requisicao.json().keys()