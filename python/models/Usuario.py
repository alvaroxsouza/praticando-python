class Usuario:
    def __init__(self, email, senha, nome="", isAdmin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.isAdmin = isAdmin

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_senha(self):
        return self.senha

    def set_senha(self, senha):
        self.senha = senha

    def get_isAdmin(self):
        return self.isAdmin

    def set_isAdmin(self, isAdmin):
        self.isAdmin = isAdmin
