from funcoes_biblioteca.cadastrar_livro import cadastrar_livro
from funcoes_biblioteca.buscar_livro import buscar_livro
from funcoes_biblioteca.emprestar_livro import emprestar_livro
from funcoes_biblioteca.devolver_livro import devolver_livro
from funcoes_biblioteca.verificar_livros_emprestados import verificar_livros_emprestados
from models.Usuario import Usuario
from persist.banco_de_dados_criacao import criar_estrutura_banco_dados
from persist.autenticar import autenticar_usuario
from persist.autenticar import criar_usuario


def menu_program():
    print("1 - Cadastrar Livro")
    print("2 - Buscar Livro")
    print("3 - Empréstimo")
    print("4 - Devolução")
    print("5 - Verificar livros emprestados")
    print("* - Sair")


def fazer_login_criar_usuario():
    print("1 - Fazer login")
    print("2 - Criar conta")
    print("* - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        usuario_login = fazer_login()
        if usuario_login != None:
            return usuario_login
        else:
            fazer_login_criar_usuario()
    elif opcao == 2:
        criar_usuario()
        fazer_login_criar_usuario()
    else:
        print("Fim da execução!")


def fazer_login():
    print("Digite seu email: ")
    email = str(input())
    print("Digite sua senha: ")
    senha = str(input())

    usuario = Usuario(email, senha)

    reposta = autenticar_usuario(usuario)

    if reposta:
        print("Logado com sucesso!")
        return reposta
    else:
        print("Email ou senha incorretos!")


def loop_principal():
    continuar_execucao = True
    while continuar_execucao:
        menu_program()
        option = int(input("Digite a opção desejada: "))
        if option == 1:
            cadastrar_livro()
            print("Livro cadastrado")
        elif option == 2:
            buscar_livro()
        elif option == 3:
            emprestar_livro()
        elif option == 4:
            devolver_livro()
        elif option == 5:
            verificar_livros_emprestados()
        else:
            continuar_execucao = False
            print("Fim da execução!")


def main():
    criar_estrutura_banco_dados()
    usuario_logado = fazer_login_criar_usuario()
    if usuario_logado != None:
        loop_principal()
    else:
        print("Fim da execução!")


if __name__ == "__main__":
    main()
