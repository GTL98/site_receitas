# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Importar os módulos para escolher e atualizar a receita --- #
from mostrar_receita import mostrar_receita
from escolher_receita import escolher_receita
from atualizar_receita import atualizar_receita


# --- Configurações da página --- #
st.set_page_config(
    page_title='Atualizar Receita - WikiReceitas',
    page_icon=Image.open('./assets/icone.png'),
    layout='wide',
    initial_sidebar_state='collapsed'
)

# --- Título da página --- #
st.title('Atualizar Receita', text_alignment='center')

# --- Selecionar qual banco de dados terá a atualização da receita --- #
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

            # --- Atualizar os ingredientes --- #
            st.subheader('Atualize os ingredientes:')
            ingredientes = st.text_area(
                label='',
                label_visibility='collapsed',
                key='ingredientes',
                height=200,
                value=conteudo_receita['ingredientes']
            )

            # --- Atualizar o modo de preparo --- #
            st.subheader('Atualize o modo de preparo:')
            modo_preparo = st.text_area(
                label='',
                label_visibility='collapsed',
                key='modo_preparo',
                height=200,
                value=conteudo_receita['modo_preparo']
            )

            # --- Botão para atualizar a receita ao banco de dados --- #
            colunas = st.columns(5)
            with colunas[2]:
                atualizar = st.button(
                    label='Atualizar',
                    key='botao_atualizar',
                    width='stretch'
                )
            if atualizar:
                atualizar_receita(
                    banco=tipo_receita,
                    nome_receita=receita,
                    ingredientes=ingredientes,
                    modo_preparo=modo_preparo
                )
                st.success(f'Receita {receita} atualizada com sucesso!')
                
except NameError:
    pass