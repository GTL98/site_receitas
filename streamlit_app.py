# --- Importar o Streamlit --- #
import streamlit as st

# --- Criar o navegador de páginas --- #
pg = st.navigation(
    [
        st.Page('./pages/home.py', title='Página Inicial'),
        st.Page('./pages/adicionar.py', title='Adicionar'),
        st.Page('./pages/atualizar.py', title='Atualizar')
    ],
)

pg.run()