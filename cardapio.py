from types import SimpleNamespace

class Prato():
    def __init__(self, nome, preco, categoria, description):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.description = description

class PratosSalgados():

    croisssant:Prato
    sanduiche_natural: Prato
    coxinha: Prato
    pastel:Prato
    crepioca:Prato
    torrada:Prato
    esfiha:Prato
    quiche:Prato
    omelete:Prato

    lista = []

    def __init__(self):
        self.croisssant =  Prato("Croissant", 7.49, "Pratos Salgados", "Massa folhada com queijo, presunto e manteiga")
        self.lista.append(self.croisssant)

        self.sanduiche_natural = Prato("Sanduíche Natural", 9.90, "Pratos Salgados", "Sanduíche com queijo, peito de peru, salada e tomate")
        self.lista.append(self.sanduiche_natural)

        self.coxinha = Prato("Coxinha de Frango", 4.90, "Pratos Salgados" , "Salgado de frango desfiado com Catupery")
        self.lista.append(self.coxinha)

        self.pastel = Prato("Calzone de carne moída", 5.35, "Pratos Salgados", "Pastel frito na hora com carne moída e queijo")
        self.lista.append(self.pastel)

        self.crepioca = Prato("Crepioca com Cottage", 8.80 , "Pratos Salgados", "Massa base de tapioca e ovo, recheada com queijo cottage cremoso")
        self.lista.append(self.crepioca)

        self.torrada = Prato("Torrada com pasta de atum", 7.49, "Pratos Salgados", "Torradas crocantes servidas com uma pasta cremosa de atum temperada" )
        self.lista.append(self.torrada)

        self.esfiha = Prato("Esfirra de carne", 5.50, "Pratos Salgados" , "Massa fina e macia, recheada com carne temperada, assada")
        self.lista.append(self.esfiha)

        self.quiche = Prato("Quiche de alho poró", 9.50, "Pratos Salgados", "4x Massa crocante recheada com creme de ovos, queijo e alho-poró refogado")
        self.lista.append(self.quiche)

        self.omelete = Prato("Omelete de 3 queijos", 9.90, "Pratos Salgados", "Ovos batidos preparados com uma mistura cremosa de três queijos")
        self.lista.append(self.omelete)
class PratosDoces():

    bomba: Prato
    croissant: Prato
    torta_l: Prato
    macaron: Prato
    cookie:Prato
    banoffee: Prato
    donut: Prato
    bolo_c:Prato
    red_v:Prato

    
    lista = []

    def __init__(self):
        self.bomba = Prato(
            "Bomba de Chocolate",
            6.90,
            "Pratos Doces",
            "Massa leve recheada com creme e coberta com uma camada de chocolate meio amargo."
        )
        self.lista.append(self.bomba)

        self.croissant = Prato(
            "Croissant de Chocolate",
            7.50,
            "Pratos Doces",
            "Massa folhada crocante recheada com chocolate cremoso,"
        )
        self.lista.append(self.croissant)

        self.torta_l = Prato(
            "Torta de Limão",
            8.90,
            "Pratos Doces",
            "Massa crocante com recheio cremoso de limão e cobertura de merengue dourado."
        )
        self.lista.append(self.torta_l)

        self.macaron = Prato(
            "Macaron",
            4.50,
            "Pratos Doces",
            "Dois discos de farinha de amêndoas com recheio cremoso."
        )
        self.lista.append(self.macaron)

        self.cookie = Prato(
            "Cookie de Chocolate",
            5.00,
            "Pratos Doces",
            "Biscoito macio por dentro e crocante por fora, com pedaços generosos de chocolate."
        )
        self.lista.append(self.cookie)

        self.banoffee = Prato(
            "Banoffee",
            9.90,
            "Pratos Doces",
            "Camadas de banana, doce de leite, chantilly e farofa crocante de biscoito."
        )
        self.lista.append(self.banoffee)

        self.donut = Prato(
            "Donut com Cobertura",
            6.00,
            "Pratos Doces",
            "Massa leve e frita, coberta com calda de chocolate ou morango e confeitos coloridos."
        )
        self.lista.append(self.donut)

        self.bolo_c = Prato(
            "Bolo de Cenoura com Chocolate",
            7.00,
            "Pratos Doces",
            "Bolo úmido de cenoura com cobertura generosa de chocolate cremoso."
        )
        self.lista.append(self.bolo_c)

        self.red_v = Prato(
            "Cupcake Red Velvet",
            6.50,
            "Pratos Doces",
            "Mini bolo aveludado com toque de cacau e cobertura suave de cream cheese doce."
        )
        self.lista.append(self.red_v)
class Bebidas():

    espresso: Prato
    cappuccino: Prato
    latte: Prato
    cha_v: Prato
    ice_coffe: Prato
    vitamina: Prato
    suco_l: Prato
    iogurte: Prato
    bobba: Prato

    lista = []

    def __init__(self):
        self.espresso = Prato(
            "Café Espresso",
            4.00,
            "Bebidas",
            "Café curto e intenso, preparado sob pressão a partir de grãos moídos na hora."
        )
        self.lista.append(self.espresso)

        self.cappuccino = Prato(
            "Cappuccino",
            6.50,
            "Bebidas",
            "Combinação equilibrada de café espresso, leite vaporizado e espuma cremosa."
        )
        self.lista.append(self.cappuccino)

        self.latte = Prato(
            "Café Latte",
            6.90,
            "Bebidas",
            "Bebida suave com café espresso e grande proporção de leite vaporizado."
        )
        self.lista.append(self.latte)

        self.cha_v = Prato(
            "Chá Verde",
            5.00,
            "Bebidas",
            "Infusão leve e refrescante, rica em antioxidantes e com sabor herbal suave."
        )
        self.lista.append(self.cha_v)

        self.ice_coffe = Prato(
            "Iced Coffee",
            7.00,
            "Bebidas",
            "Café espresso servido gelado com leite e cubos de gelo. Refrescante e intenso."
        )
        self.lista.append(self.ice_coffe)

        self.vitamina = Prato(
            "Vitamina de Banana com Aveia",
            8.50,
            "Bebidas",
            "Bebida nutritiva feita com banana, leite e aveia, ideal para começar o dia."
        )
        self.lista.append(self.vitamina)

        self.suco_l = Prato(
            "Suco Natural de Laranja",
            6.00,
            "Bebidas",
            "Suco 100% natural feito com laranjas frescas, sem adição de açúcar."
        )
        self.lista.append(self.suco_l)

        self.iogurte = Prato(
            "Iogurte com Frutas Vermelhas",
            7.90,
            "Bebidas",
            "Iogurte batido com frutas vermelhas e leve toque de mel. Cremoso e saudável."
        )
        self.lista.append(self.iogurte)

        self.bobba = Prato(
            "Bobba Tea (Chá com Pérolas)",
            9.50,
            "Bebidas",
            "Chá gelado adoçado com leite e servido com pérolas de tapioca. Doce, divertido e refrescante."
        )
        self.lista.append(self.bobba)

class Cardapio():
    
    pratos_salgados:PratosSalgados = PratosSalgados()
    pratos_doces: PratosDoces = PratosDoces()
    bebidas: Bebidas = Bebidas()
    

    