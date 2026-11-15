import sqlite3

# Criar db/tabela:


conn = sqlite3.connect("produtos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL DEFAULT 0,
    codigo_barras TEXT UNIQUE,
    categoria TEXT,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")



# Inserir dados:

cursor.execute("""
INSERT INTO produtos
(nome, preco, estoque)
VALUES (?, ?, ?)
""", (
    "Notebook Dell",
    "Notebook i7 16GB RAM",
    4500.00,
    10,
    "Informática"
))