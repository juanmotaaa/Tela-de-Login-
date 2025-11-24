import sqlite3

con = sqlite3.connect("sistema.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
""")

# --- INSERIR USUÁRIO PADRÃO ---
cur.execute("INSERT OR IGNORE INTO usuarios (usuario, senha) VALUES (?, ?)", ("admin", "123"))
con.commit()
# -------------------------------

def adicionar_usuario(usuario, senha):
    cur.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
    con.commit()

def buscar_usuario(usuario, senha):
    cur.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha))
    return cur.fetchone()

def listar_usuarios():
    cur.execute("SELECT id, usuario FROM usuarios")
    return cur.fetchall()

def atualizar_usuario(id_, usuario, senha):
    cur.execute("UPDATE usuarios SET usuario=?, senha=? WHERE id=?", (usuario, senha, id_))
    con.commit()

def excluir_usuario(id_):
    cur.execute("DELETE FROM usuarios WHERE id=?", (id_,))
    con.commit()

print("Usuários existentes no banco:", listar_usuarios())
