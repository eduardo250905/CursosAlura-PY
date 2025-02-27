from item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
    
    def __str__(self):
        return f'{self._nome}: R${self._preco} | {self._tipo} | {self._tamanho}'

    def aplicar_desconto(self):
        pass

sobremesa = Sobremesa('sorvete', 10, 'casquinha', 'médio')
print(sobremesa)
