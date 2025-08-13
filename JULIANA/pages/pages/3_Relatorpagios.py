import streamlit as st
import pandas as pd
import plotly.express as px
from db import listar_consultas

st.title("📊 Relatórios")

consultas = listar_consultas()
if not consultas:
    st.info("Nenhuma consulta registrada para gerar relatório.")
else:
    df = pd.DataFrame(consultas, columns=["ID", "PacienteID", "Data", "Status", "Notas"])

    st.markdown("**Resumo por status**")
    fig = px.histogram(df, x="Status", title="Status das Consultas")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("**Consultas por data**")
    df_count = df.groupby("Data").size().reset_index(name="Quantidade")
    fig2 = px.line(df_count, x="Data", y="Quantidade", title="Consultas por Data")
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("**Tabela completa**")
    st.dataframe(df)