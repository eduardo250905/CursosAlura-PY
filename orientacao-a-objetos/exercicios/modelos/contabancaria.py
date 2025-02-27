class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f'Titular: {self._titular}, Saldo: R${self._saldo}'

    @classmethod
    def ativar_conta(cls, self):
        self._ativo = True

pessoa1 = ContaBancaria('Eduardo', 1300)
pessoa2 = ContaBancaria('Gustavo', 750)
print(pessoa1)
print(pessoa2)
pessoa1.ativar_conta()
print(pessoa1._ativo)
