import sqlite3
import os
if os.path.exists('teste.db'):
    os.remove('teste.db')

#cria o arquivo
conexao = sqlite3.connect('teste.db')

#criar cursor pra percorrer os registros
cursor = conexao.cursor()

#criar a tabela com os parametros
criarTabela = 'CREATE TABLE COMANDAS ( id INTEGER PRIMARY KEY AUTOINCREMENT, id_comanda INTEGER, pedido TEXT, preco REAL )'
cursor.execute(criarTabela)
conexao.commit()

def addPedido(id_comanda, pedido, preco):
    cursor.execute("INSERT INTO COMANDAS (id_comanda, pedido, preco) VALUES (?, ?, ?)", (id_comanda, pedido, preco))
    conexao.commit()

def excluir_pedido(id_comanda, pedido):
    cursor.execute('DELETE FROM COMANDAS WHERE id_comanda = ? AND pedido = ? ', (id_comanda, pedido,))
    conexao.commit()

addPedido(1, 'Hamburguer', 39.90)
def total_comanda(id_comanda):
    cursor.execute('SELECT SUM(preco) FROM COMANDAS WHERE id_comanda = ? ', (id_comanda,))
    total = cursor.fetchone()[0]
    return total if total else 00.00

def pedidos_comanda(id_comanda): #daria pra fazer colocando o pedido e o preco ao lado se quiser
    cursor.execute('SELECT pedido FROM COMANDAS WHERE id_comanda = ?', (id_comanda,))
    pedidos = cursor.fetchall()
    lista = []
    for pedido in pedidos:
        lista.append(pedido[0])
    return lista if lista else 'Não há pedidos feitos nessa comanda.'



addPedido(1, 'risoto', 60.00)
addPedido(1, 'macarrao', 90.00)
print(pedidos_comanda(2))
excluir_pedido(1, 'risoto')
print(pedidos_comanda(1))