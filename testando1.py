import tkinter as tk
from functools import partial

def reiniciar():
    for frame in frame1.winfo_children():
        frame.pack_forget()

root = tk.Tk()

frame1 = tk.Frame(None)
frame1.pack()


num_comanda=tk.StringVar()


def confirmar():
    global frame2
    global frame3
    global label2
    global comanda
    comanda=Pedido(num_comanda.get())
    print(comanda)
    num_comanda.set("")
    for k in tela1:
        k.destroy()
    frame3 = tk.Frame(root, bg="white")
    frame3.place(relwidth=0.3,relheight=0.8, relx=0, rely=0.1)
    label1 = tk.Label(frame3, text=(f"Pedidos da comanda {comanda.comanda}"))
    label1.pack()
    label2 = tk.Label(frame3, text=(f"Total {comanda.total}"))
    label2.place(rely=1)
    label2.pack()
    frame2 = tk.Frame(root, bg="white")
    frame2.place(relwidth=0.6,relheight=0.8, relx=0.4, rely=0.1)
    adicionar1 = tk.Button(frame2, text='Adicionar hambúrguer ao pedido', padx=10, pady=5, fg='white', bg='#263D42', command=partial(comanda.ad_prato, prato1))
    adicionar1.pack()
    adicionar2 = tk.Button(frame2, text='Adicionar batata frita ao pedido', padx=10, pady=5, fg='white', bg='#263D42', command=partial(comanda.ad_prato, prato2))
    adicionar2.pack()
    voltar = tk.Button(frame1, text='Voltar à tela inicial', padx=10, pady=5, fg='white', bg='#263D42', command=reiniciar())
    voltar.pack()

    

comanda_label = tk.Label(root, text = 'Número da comanda:', font=('calibre',10, 'bold'))
comanda_entry = tk.Entry(root,textvariable = num_comanda, font=('calibre',10,'normal'))
confirmar_btn=tk.Button(root,text = 'Confirmar', command = confirmar)
comanda_label.pack()
comanda_entry.pack()
confirmar_btn.pack()
tela1=[comanda_label,comanda_entry, confirmar_btn]



class Pedido():
    def __init__(self, comanda):
        for widget in frame1.winfo_children():
            widget.destroy()
        self.comanda = comanda
        self.itens = []
        self.total=0
        self.qtde_itens=0
    def ad_prato(self, prato):
        self.nome=prato.nome
        prato.quantidade += 1
        print(prato.quantidade)
        self.qtde_itens +=1
        print(self.qtde_itens)
        self.total+=prato.preco
        label2.config(text=(f"Total {comanda.total}"))
        self.itens.append(self.nome)
        label = tk.Label(frame3, text=self.nome, bg='gray')
        label.pack()

cardapio = {}        
class Pratos():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.quantidade=0
        cardapio[self.nome]=self.preco

prato1 = Pratos('Hambúrguer', 40)
prato2 = Pratos('Batata Frita', 15)

root.mainloop()



