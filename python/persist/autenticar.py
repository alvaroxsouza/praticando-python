import sqlite3
from models.Usuario import Usuario


def autenticar_usuario(usuario: Usuario):
    conn = sqlite3.connect("banco_de_dados.db")
    cursor = conn.cursor()

    cursor.execute(
        """ select * from usuario where email = ? and senha = ?""",
        (
            usuario.get_email(),
            usuario.get_senha(),
        ),
    )

    resposta = cursor.fetchone()
    conn.commit()
    conn.close()

    return resposta


def criar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    usuario_criado = Usuario(email, senha, nome, False)

    insert_usuario_banco_dados(usuario_criado)


def insert_usuario_banco_dados(usuario: Usuario):
    conn = sqlite3.connect("banco_de_dados.db")
    cursor = conn.cursor()

    cursor.execute(
        """ INSERT INTO usuario VALUES (NULL, ?, ?, ?, ?) """,
        (
            usuario.get_nome(),
            usuario.get_email(),
            usuario.get_senha(),
            usuario.get_isAdmin(),
        ),
    )

    conn.commit()
    conn.close()
