import streamlit as st
from db import add_paciente, listar_pacientes
import pandas as pd

st.title("📋 Cadastro de Pacientes")

with st.form("form_paciente", clear_on_submit=True):
    nome = st.text_input("Nome")
    idade = st.number_input("Idade", min_value=0, max_value=120, value=30)
    contato = st.text_input("Contato (telefone/email)")
    observacoes = st.text_area("Observações")
    submitted = st.form_submit_button("Salvar Paciente")

if submitted:
    if nome.strip():
        add_paciente(nome.strip(), int(idade), contato.strip(), observacoes.strip())
        st.success("Paciente cadastrado com sucesso!")
    else:
        st.error("O nome é obrigatório.")

st.subheader("Pacientes cadastrados")
pacientes = listar_pacientes()
if pacientes:
    df = pd.DataFrame(pacientes, columns=["ID", "Nome", "Idade", "Contato", "Observações"])
    st.dataframe(df)
else:
    st.info("Nenhum paciente cadastrado ainda.")