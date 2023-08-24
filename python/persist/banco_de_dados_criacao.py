import sqlite3

from models.Usuario import Usuario


def criar_banco():
    conn = sqlite3.connect("banco_de_dados.db")
    conn.commit()
    conn.close()


def criar_tabela_usuarios():
    conn = sqlite3.connect("banco_de_dados.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuario 
        (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT UNIQUE,
            senha TEXT,
            isAdmin INTEGER
        )
        """
    )

    conn.commit()
    conn.close()


def criar_tabela_livros():
    conn = sqlite3.connect("banco_de_dados.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS livro
        (
            id INTEGER PRIMARY KEY,
            titulo TEXT,
            autor TEXT,
            isbn TEXT,
            quantidade_exemplares INTEGER
        )
        """
    )
    conn.commit()
    conn.close()


def criar_tabela_emprestimos():
    conn = sqlite3.connect("banco_de_dados.db")
    cursor = conn.cursor()

    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS emprestimo 
        (
            id INTEGER PRIMARY KEY,
            id_usuario INTEGER,
            id_livro INTEGER,
            data_emprestimo TEXT,
            FOREIGN KEY(id_usuario) REFERENCES usuario(id),
            FOREIGN KEY(id_livro) REFERENCES livro(id)
        )
        """
    )

    conn.commit()
    conn.close()


def criar_usuario_master():
    conn = sqlite3.connect("banco_de_dados.db")
    cursor = conn.cursor()

    usuario_master = Usuario("master", "master", "master", True)

    cursor.execute(
        """ select * from usuario where email = ? and senha = ?""",
        (
            usuario_master.get_email(),
            usuario_master.get_senha(),
        ),
    )

    if cursor.fetchone() == None:
        cursor.execute(
            """ INSERT INTO usuario VALUES (NULL, ?, ?, ?, ?) """,
            (
                usuario_master.get_nome(),
                usuario_master.get_email(),
                usuario_master.get_senha(),
                usuario_master.get_isAdmin(),
            ),
        )
        conn.commit()

    conn.close()


def criar_estrutura_banco_dados():
    criar_banco()
    criar_tabela_usuarios()
    criar_usuario_master()
    criar_tabela_livros()
    criar_tabela_emprestimos()


if __name__ == "__main__":
    criar_estrutura_banco_dados()
