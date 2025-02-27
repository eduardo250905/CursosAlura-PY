from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Maracujá', 10.0, 'Grande')
prato_pao = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)

bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
