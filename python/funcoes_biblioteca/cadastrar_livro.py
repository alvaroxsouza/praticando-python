from models.Livro import Livro
from persist.banco_de_dados_insert import insert_livro_banco_dados


def criar_livro(titulo, autor, isbn, quantidade_exemplares=0):
    livro = Livro(titulo, autor, isbn, quantidade_exemplares)
    return livro


def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    isbn = input("Digite o ISBN: ")
    quantidade_exemplares = int(input("Digite a quantidade de exemplares: "))

    insert_livro_banco_dados(criar_livro(titulo, autor, isbn, quantidade_exemplares))
