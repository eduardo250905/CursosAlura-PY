class Livro:
    def __init__(self, titulo, autor, ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = True

    def __str__(self):
        return f'O livro {self._titulo}, escrito por {self._autor} foi publicado em {self._ano_publicado}'

    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicado == ano and livro._disponivel]
        return livros_disponiveis
