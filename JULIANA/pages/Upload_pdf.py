import streamlit as st
import os
from db import atualizar_pdf

st.set_page_config(page_title="Upload de PDFs", layout="wide")

st.title("📄 Upload de PDFs do Atendimento")

# Captura o ID do atendimento pela URL
query_params = st.query_params
atendimento_id = query_params.get("id")

if atendimento_id:
    tipo_pdf = st.radio("Tipo de PDF", ["Laudo", "Avaliação"])
    arquivo = st.file_uploader("Selecione o PDF", type=["pdf"])

    if arquivo:
        pasta = os.path.join("data", "pdfs")
        os.makedirs(pasta, exist_ok=True)
        caminho_pdf = os.path.join(pasta, f"{tipo_pdf}_{atendimento_id}.pdf")

        with open(caminho_pdf, "wb") as f:
            f.write(arquivo.read())

        atualizar_pdf(atendimento_id, tipo_pdf.lower(), caminho_pdf)
        st.success(f"{tipo_pdf} enviado com sucesso!")
else:
    st.error("Nenhum ID de atendimento foi informado.")