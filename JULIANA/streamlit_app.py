import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="JULIANA - MVP",
    page_icon="💼",
    layout="centered"
)

# Título e descrição
st.title("💼 JULIANA ")
st.markdown(
    """
    ### Sistema de Gestão Simplificado  
    Bem-vindo ao **MVP do Sistema JULIANA**.  
    Escolha abaixo a área que deseja acessar.
    """
)

# Botões de navegação
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("👩‍⚕️ Pacientes"):
        st.switch_page("pages/pages/1_Pacientes.py")

with col2:
    if st.button("📅 Agenda"):
        st.switch_page("pages/pages/2_Agenda.py")

with col3:
    if st.button("📊 Relatórios"):
        st.switch_page("pages/pages/3_Relatorpagios.py")

# Rodapé
st.markdown("---")
st.caption("Versão MVP - Desenvolvido para demonstração")
