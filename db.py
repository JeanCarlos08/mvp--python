import sqlite3
import os

# Caminho do banco de dados
DB_PATH = os.path.join(os.path.dirname(__file__), "data", "atendimentos.db")

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_conn()
    c = conn.cursor()

    # Criação da tabela de atendimentos
    c.execute("""
    CREATE TABLE IF NOT EXISTS atendimentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        empresa TEXT NOT NULL,
        nome TEXT NOT NULL,
        modalidade TEXT NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL,
        laudo_pdf TEXT,
        avaliacao_pdf TEXT
    )
    """)

    conn.commit()
    conn.close()

def inserir_atendimento(empresa, nome, modalidade, data, hora):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        INSERT INTO atendimentos (empresa, nome, modalidade, data, hora)
        VALUES (?, ?, ?, ?, ?)
    """, (empresa, nome, modalidade, data, hora))
    conn.commit()
    conn.close()

def listar_atendimentos():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM atendimentos")
    rows = c.fetchall()
    conn.close()
    return rows

def atualizar_pdf(atendimento_id, tipo, caminho_pdf):
    conn = get_conn()
    c = conn.cursor()
    if tipo == "laudo":
        c.execute("UPDATE atendimentos SET laudo_pdf = ? WHERE id = ?", (caminho_pdf, atendimento_id))
    elif tipo == "avaliacao":
        c.execute("UPDATE atendimentos SET avaliacao_pdf = ? WHERE id = ?", (caminho_pdf, atendimento_id))
    conn.commit()
    conn.close()