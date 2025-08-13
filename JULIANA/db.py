import sqlite3
def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    c = conn.cursor()

    # Tabela de pacientes
    c.execute('''CREATE TABLE IF NOT EXISTS pacientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER,
                    contato TEXT,
                    observacoes TEXT
                )''')

    # Tabela de consultas
    c.execute('''CREATE TABLE IF NOT EXISTS consultas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    paciente_id INTEGER,
                    data TEXT,
                    status TEXT,
                    notas TEXT,
                    FOREIGN KEY(paciente_id) REFERENCES pacientes(id)
                )''')
    conn.commit()
    conn.close()

# CRUD pacientes
def add_paciente(nome, idade, contato, observacoes):
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO pacientes (nome, idade, contato, observacoes) VALUES (?, ?, ?, ?)",
              (nome, idade, contato, observacoes))
    conn.commit()
    conn.close()

def listar_pacientes():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT id, nome, idade, contato, observacoes FROM pacientes ORDER BY nome")
    data = c.fetchall()
    conn.close()
    return data

# CRUD consultas
def add_consulta(paciente_id, data, status, notas):
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO consultas (paciente_id, data, status, notas) VALUES (?, ?, ?, ?)",
              (paciente_id, data, status, notas))
    conn.commit()
    conn.close()

def listar_consultas():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT id, paciente_id, data, status, notas FROM consultas ORDER BY data")
    data = c.fetchall()
    conn.close()
    return data