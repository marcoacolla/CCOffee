from cardapio import Cardapio

for item in Cardapio.cardapio:
    acessItem = Cardapio.cardapio[item]
    print(acessItem.nome)