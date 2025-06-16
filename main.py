from cardapio import Cardapio
#from types import SimpleNamespace

print("Pratos Salgados: ")
for salgado in Cardapio.pratos_salgados.lista:
    print(salgado.nome)
print("")
print("Pratos Doces:")
for item in Cardapio.pratos_doces.lista:
    print(item.nome)
print("")
print("Bebidas:")
for bebida in Cardapio.bebidas.lista:
    print(bebida.nome)
