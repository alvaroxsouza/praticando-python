class Livro:
    def __init__(self, titulo, autor, isbn, quantidade_exemplares=0):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.quantidade_exemplares = quantidade_exemplares

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_quantidade_exemplares(self):
        return self.quantidade_exemplares

    def set_quantidade_exemplares(self, quantidade_exemplares):
        self.quantidade_exemplares = quantidade_exemplares
