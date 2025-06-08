class Prato():
    def __init__(self, nome, preco, categoria, description):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.description = description
    
class Cardapio():
    cardapio = {
        "spaghetti": Prato("Spaghetti a Bolonhesa", 28.50, "Pratos Salgados", "Massa com molho bolonhesa e parmesão"),
        "frango": Prato("Frango Grelhado", 19.90,"Pratos Salgados", "Peito de frango grelhado com legumes.")
    }

    