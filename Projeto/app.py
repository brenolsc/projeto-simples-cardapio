from modelos.restaurante import Restaurante
from cardapio.bebida import Bebida
from cardapio.prato import Prato

restaurante_praca = Restaurante('praca', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Medio')
bebida_suco.aplicar_desconto()
prato_baguete = Prato('Baguete', 2.00, 'O melhor baguete da cidade')
prato_baguete.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_baguete)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()