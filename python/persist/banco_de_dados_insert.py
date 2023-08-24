import sqlite3

from models.Livro import Livro


def insert_livro_banco_dados(livro: Livro):
    conn = sqlite3.connect("banco_de_dados.db")
    cursor = conn.cursor()

    cursor.execute(
        """ INSERT INTO livros VALUES (NULL, ?, ?, ?, ?) """,
        (
            livro.get_titulo(),
            livro.get_autor(),
            livro.get_isbn(),
            livro.get_quantidade_exemplares(),
        ),
    )

    conn.commit()
    conn.close()
