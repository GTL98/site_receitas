# --- Importar as bibliotecas --- #
import requests
import streamlit as st


def mostrar_receita(banco: str, receita: str) -> dict:
    """
    Função responsável por mostrar a receita.
    :param banco: Banco da receita selecionada ('doce', 'salgado', 'paes')
    :param receita: Receita selecionada pelo usuário.
    :return:
    """
    # --- Link do banco de dados --- #
    link = 'https://wikireceitas-aace2-default-rtdb.firebaseio.com/'

    # --- Obter as receitas --- #
    dic_requisicao = requests.get(f'{link}/{banco}/{receita}.json')

    return dic_requisicao.json()