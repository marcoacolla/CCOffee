class Prato():
    def __init__(self, nome, preco, description):
        self.nome = nome
        self.preco = preco
        self.description = description
    
class Cardapio():
    cardapio = {
        "spaghetti": Prato("Spaghetti a Bolonhesa", 28.50, "Massa com molho bolonhesa e parmesão"),
        "frango": Prato("Frango Grelhado", 19.90, "Peito de frango grelhado com legumes.")
    }

    