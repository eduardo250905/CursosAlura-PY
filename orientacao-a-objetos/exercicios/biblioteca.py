from modelos.livro import Livro

livro1 = Livro('Livro 1', 'Livro 2', 20)
livro1.emprestar()
print(f'{livro1._disponivel}')
