# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Importar os módulos criados --- #
from mostrar_receita import mostrar_receita
from escolher_receita import escolher_receita

# --- Configurações da página --- #
st.set_page_config(
    page_title='Página Inicial - WikiReceitas',
    page_icon=Image.open('./assets/icone.png'),
    layout='wide',
    initial_sidebar_state='collapsed'
)

# --- Título da página --- #
st.title('WikiReceitas', text_alignment='center')

# --- Selecionar o tipo de receita --- #
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

# --- Verificar se foi selecionado o tipo de receita --- #
try:
    if tipo_receita:
        # --- Selecionar o tipo de receita --- #
        receitas = escolher_receita(tipo_receita)
        st.subheader('Escolha a receita:')
        receita = st.selectbox(
            label='',
            options=receitas,
            key='receita',
            label_visibility='collapsed',
            placeholder='Escolha a receita desejada...',
            index=None
        )

        if receita:
            # --- Obter o conteúdo do banco de dados --- #
            conteudo_receita = mostrar_receita(tipo_receita, receita)

            # --- Nome da receita --- #
            st.header(receita)

            # --- Ingredientes --- #
            with st.container(border=True):
                st.subheader('Ingredientes:')
                st.write(conteudo_receita['ingredientes'])

            # --- Modo de preparo --- #
            with st.container(border=True):
                st.subheader('Modo de preparo:')
                st.write(conteudo_receita['modo_preparo'])
except NameError:
    pass
