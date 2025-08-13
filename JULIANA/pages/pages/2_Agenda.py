import streamlit as st
from db import listar_pacientes, add_consulta, listar_consultas
from datetime import date
import pandas as pd

st.title("📅 Agenda de Consultas")

pacientes = listar_pacientes()
if not pacientes:
    st.info("Cadastre pacientes primeiro na página 'Pacientes'.")
else:
    opcoes = {p[1]: p[0] for p in pacientes}  # nome → id
    with st.form("form_agenda", clear_on_submit=True):
        paciente_nome = st.selectbox("Paciente", list(opcoes.keys()))
        data_consulta = st.date_input("Data", date.today())
        status = st.selectbox("Status", ["Agendado", "Concluído", "Cancelado"])
        notas = st.text_area("Notas da sessão")
        submitted = st.form_submit_button("Agendar Consulta")

    if submitted:
        add_consulta(opcoes[paciente_nome], str(data_consulta), status, notas)
        st.success("Consulta registrada com sucesso!")

st.subheader("Consultas registradas")
consultas = listar_consultas()
if consultas:
    df = pd.DataFrame(consultas, columns=["ID", "PacienteID", "Data", "Status", "Notas"])
    st.dataframe(df)
else:
    st.info("Nenhuma consulta registrada ainda.")