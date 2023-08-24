from funcoes_biblioteca import cadastrar_livro
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
    print("6 - Sair")


def fazer_login_criar_usuario():
    print("1 - Fazer login")
    print("2 - Criar conta")
    print("* - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        fazer_login()
    elif opcao == 2:
        criar_usuario()
        fazer_login_criar_usuario()
    else:
        print("Fim da execução!")


def fazer_login():
    print("Digite seu email: ")
    email = input()
    print("Digite sua senha: ")
    senha = input()

    usuario = Usuario(email, senha)

    reposta = autenticar_usuario(usuario)

    if reposta:
        print("Logado com sucesso!")
    else:
        print("Email ou senha incorretos!")


def loop_principal():
    continuar_execucao = True
    while continuar_execucao:
        menu_program()
        option = int(input("Digite a opção desejada: "))
        if option == 1:
            livro = cadastrar_livro()
        # elif option == 2:
        #     buscar_livro()
        # elif option == 3:
        #     emprestar_livro()
        # elif option == 4:
        #     devolver_livro()
        # elif option == 5:
        #     verificar_livros_emprestados()
        else:
            continuar_execucao = False
            print("Fim da execução!")


def main():
    criar_estrutura_banco_dados()
    fazer_login_criar_usuario()
    loop_principal()


if __name__ == "__main__":
    main()
