import streamlit as st
import pandas as pd
import os
from db import init_db, listar_atendimentos, inserir_atendimento

# Configuração da página
st.set_page_config(page_title="Gestão Clínica", page_icon="💼", layout="wide")

# Inicializa o banco de dados
init_db()

st.title("💼 JULIANA - MVP")
st.markdown("### Sistema de Gestão Simplificado")

# Formulário para adicionar atendimento
with st.expander("➕ Adicionar Atendimento"):
    with st.form(key="form_atendimento"):
        col1, col2 = st.columns(2)
        empresa = col1.text_input("Empresa")
        nome = col2.text_input("Nome")
        modalidade = col1.selectbox("Modalidade", ["Admissional", "Periódico", "Demissional"])
        data = col2.date_input("Data")
        hora = col1.time_input("Hora")
        submitted = st.form_submit_button("Salvar")

        if submitted and empresa and nome:
            inserir_atendimento(empresa, nome, modalidade, data.strftime("%d/%m/%Y"), hora.strftime("%H:%M"))
            st.success("Atendimento adicionado!")
            st.rerun()

# Lista de atendimentos
dados = listar_atendimentos()
df = pd.DataFrame(dados, columns=["ID", "Empresa", "Nome", "Modalidade", "Data", "Hora", "Laudo PDF", "Avaliação PDF"])

# Transforma nome em link para upload de PDFs
def criar_link_upload(row):
    return f"[{row['Nome']}](/Upload_PDF?id={row['ID']})"

if not df.empty:
    df["Nome"] = df.apply(criar_link_upload, axis=1)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Nenhum atendimento registrado")