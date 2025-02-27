class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao.upper()
    
    def __str__(self):
        return f'Nome: {self._nome}\nIdade: {self._idade}\nProfissão: {self._profissao}'

    @property
    def saudacao(self):
        return f'Olá, sou {self._nome} e trabalho com {self._profissao}'

    def aniversario(self):
        self._idade += 1

eduardo = Pessoa('Eduardo', 19, 'Programador')
print(eduardo)
eduardo.aniversario()
print(eduardo.saudacao)
