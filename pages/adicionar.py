# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Importar o módulo de adicionar a receita --- #
from adicionar_receita import adicionar_receita

# --- Configurações da página --- #
st.set_page_config(
    page_title='Adicionar Receita - WikiReceitas',
    page_icon=Image.open('./assets/icone.png'),
    layout='wide',
    initial_sidebar_state='collapsed'
)

# --- Título da página --- #
st.title('Adicionar Receita', text_alignment='center')

# --- Selecionar qual banco de dados irá a receita --- #
st.subheader('Escolha o tipo de receita:')
try:
    tipo_receita = st.pills(
        label='',
        options=['Doce', 'Salgado', 'Pães'],
        selection_mode='single',
        label_visibility='collapsed',
        key='tipo_receita',
        width='stretch'
    ).lower().replace('ã', 'a')
except AttributeError:
    pass

# --- Verificar se foi selecionado o tipo da receita --- #
try:
    if tipo_receita:
        # --- Informar o nome da receita --- #
        st.subheader('Digite o nome da receita:')
        nome_receita = st.text_input(
            label='',
            label_visibility='collapsed',
            key='nome_receita',
            placeholder='Digite o nome da receita...'
        )

        # --- Informar os ingredientes --- #
        st.subheader('Digite os ingredientes:')
        ingredientes = st.text_area(
            label='',
            label_visibility='collapsed',
            key='ingredientes',
            height=200
        )

        # --- Informar o modo de preparo --- #
        st.subheader('Digite o modo de preparo:')
        modo_preparo = st.text_area(
            label='',
            label_visibility='collapsed',
            key='modo_preparo',
            height=200
        )

        # --- Botão para enviar a receita ao banco de dados --- #
        colunas = st.columns(5)
        with colunas[2]:
            enviar = st.button(
                label='Enviar',
                key='botao_enviar',
                width='stretch'
            )
        if enviar:
            adicionar_receita(
                banco=tipo_receita,
                nome_receita=nome_receita,
                ingredientes=ingredientes,
                modo_preparo=modo_preparo
            )
except NameError:
    pass
