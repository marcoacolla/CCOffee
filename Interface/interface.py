import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image


LARGEFONT =("Verdana", 25)


class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        
        global inicio

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 
        container.config(width=1000, height=800)
        container.grid_propagate(0)
 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
 
        # initializing frames to an empty array
        self.frames = {}  
 
        # iterating through a tuple consisting
        # of the different page layouts
        
        for F in (Inserir_Comanda, Menu_Pedidos):
 
            frame = F(container, self)
 
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
            frame.grid(row = 0, column = 0, sticky ="nsew")

        inicio=True
        self.show_frame(Inserir_Comanda)
        
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        global inicio

        if cont==Menu_Pedidos:
            inicio=False
            global comanda
            global num_comanda
            comanda=num_comanda.get()
            label_pedidos.config(text=('PEDIDOS DA COMANDA %s' % comanda))

        elif cont==Inserir_Comanda and inicio==False:
            inicio=True
            global valor_total, pedidos_da_comanda, frame_lista_pedidos, frame_escolha, label_valor_total
            num_comanda=tk.StringVar()
            comanda_entry.config(textvariable=num_comanda)
            valor_total=0
            pedidos_da_comanda={}
            for widget in frame_lista_pedidos.winfo_children():
                widget.destroy()
            Menu_Pedidos.show_frame_cardapio(Menu_Pedidos, frame_escolha)
            label_valor_total.config(text=('Total: R$ %.2f' % valor_total))
            
 
# first window frame startpage
class Inserir_Comanda(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        global comanda, num_comanda, comanda_entry
        
        num_comanda=tk.StringVar()
        num_comanda.set("")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        

        def fit_image_to_window(image_path, window_size):
            # Load the image
            image_inicio=Image.open(image_path)
            image_width, image_height = image_inicio.size
            
            # Calculate the aspect ratio
            aspect_ratio = image_width / image_height
            
            # Get the window size
            window_width, window_height = window_size
            
            # Calculate new size keeping the aspect ratio
            if (window_width / window_height) > aspect_ratio:
                new_width = int(window_height * aspect_ratio)
                new_height = window_height
            else:
                new_width = window_width
                new_height = int(window_width / aspect_ratio)
            
            # Resize the image
            resized_image = image_inicio.resize((new_width, new_height), Image.LANCZOS)
            return ImageTk.PhotoImage(resized_image)

        def update_image(event):
            new_image_inicio = fit_image_to_window(image_path, (event.width, event.height))
            background_label_inicio.pack(fill=BOTH, expand = YES)
            background_label_inicio.config(image=new_image_inicio)
            background_label_inicio.image = new_image_inicio  # Avoid garbage collection

        image_path="/home/stella/Downloads/cafeteria(1).png"

        bg_inicio=fit_image_to_window(image_path, (700, 700))
        background_label_inicio = tk.Label(self, image = bg_inicio)
        background_label_inicio.place(x=0, y=0, relwidth=1, relheight=1)
        background_label_inicio.image = bg_inicio

        self.bind('<Configure>', update_image)


        frame_inserir_comanda=tk.Frame(self, bg='#926956', bd=2)
        frame_inserir_comanda.config(width= 400, height=200)
        frame_inserir_comanda.place(anchor='c', relx=0.5, rely=0.5)
        frame_inserir_comanda.grid_propagate(0)
        
        comanda_label = tk.Label(frame_inserir_comanda, text = 'Número da comanda:', font=('calibre',25, 'bold'), fg="#FDF3DC", bg='#926956')
        comanda_label.pack(side='top')

        comanda_entry = tk.Entry(frame_inserir_comanda, textvariable = num_comanda, font=('calibre',25), bg='#FDF3DC', fg='#70391F')
        comanda_entry.pack(side='top')

        confirmar_btn=tk.Button(frame_inserir_comanda,text = 'Confirmar', font = ('calibre',20), bg='#FDF3DC', fg='#70391F',
        command = lambda : controller.show_frame(Menu_Pedidos))
        confirmar_btn.pack(side='bottom')
         

 
# second window frame Menu Pedidos 
class Menu_Pedidos(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)

        frame_menu_pedidos=tk.Frame(self)
        frame_menu_pedidos.place(anchor='center', relx=0.5, rely=0.5)
        
        
        global label_pedidos, valor_total, pedidos_da_comanda, frame_lista_pedidos, frame_escolha, frame_cardapio, label_valor_total, dicio_frames_menu
        valor_total = 0
        pedidos_da_comanda = {}

        def fit_image_to_window(image_path, window_size):
            # Load the image
            image_menu=Image.open(image_path)
            image_width, image_height = image_menu.size
            
            # Calculate the aspect ratio
            aspect_ratio = image_width / image_height
            
            # Get the window size
            window_width, window_height = window_size
            
            # Calculate new size keeping the aspect ratio
            if (window_width / window_height) > aspect_ratio:
                new_width = int(window_height * aspect_ratio)
                new_height = window_height
            else:
                new_width = window_width
                new_height = int(window_width / aspect_ratio)
        

            # Resize the image
            resized_image = image_menu.resize((new_width, new_height), Image.LANCZOS)
            return ImageTk.PhotoImage(resized_image)


        def update_image(event):
            new_image_menu = fit_image_to_window(image_path, (event.width, event.height))
            background_label_menu.pack(fill=BOTH, expand = YES)
            background_label_menu.config(image=new_image_menu)
            background_label_menu.image = new_image_menu  # Avoid garbage collection

        image_path="/home/stella/Downloads/cafeteria(2).jpg"

        bg_menu=fit_image_to_window(image_path, (700, 700))
        background_label_menu = tk.Label(frame_menu_pedidos, image = bg_menu)
        background_label_menu.pack()
        background_label_menu.image = bg_menu

        self.bind('<Configure>', update_image)
        

        frame_cardapio = tk.Frame(frame_menu_pedidos, bg='#F6C7B3', bd=2)
        frame_cardapio.place(relwidth=0.6, relheight=0.8, relx=0.4, rely=0.1)

        label_cardapio = tk.Label(frame_cardapio, text='CARDÁPIO', font=('calibre',25, 'bold'), bg='#F6C7B3', fg="#CE724B")
        label_cardapio.pack(side='top')


        frame_pedidos = tk.Frame(frame_menu_pedidos, bg='#F6C7B3', bd=2)
        frame_pedidos.place(relwidth=0.35, relheight=0.8, relx=0, rely=0.1)        
    
        label_pedidos = tk.Label(frame_pedidos, text=('PEDIDOS DA COMANDA' ), font=('calibre',20, 'bold'), bg='#F6C7B3', fg='#CE724B')
        label_pedidos.pack( side='top')

        frame_lista_pedidos=tk.Frame(frame_pedidos, bg='#F6C7B3')
        frame_lista_pedidos.place(relx=0.05, rely=0.1)

        def ad_prato (prato, label):
            global pedidos_da_comanda, valor_total
               
            pedidos_da_comanda[prato]+=1
            preco=pratos[prato][0]
            label.pack(side='top', anchor='nw')
            label.config(text=('• %s: %d' % (prato, pedidos_da_comanda[prato])),font = ('calibre',15, 'bold'), bg='#F6C7B3', fg="#CE724B" )
            valor_total+=preco
            label_valor_total.config(text=('Total: R$ %.2f' % valor_total))

        label_valor_total = tk.Label(frame_pedidos, text=('Total: %.2f' % valor_total), font = ('calibre',20, 'bold'), bg='#CE724B', fg = "#FFD1BE")
        label_valor_total.pack(side='bottom')

        voltar_inicio_btn=tk.Button(frame_menu_pedidos, text = 'Voltar ao início', font = ('calibre',18), bg = '#F6C7B3', fg = '#CE724B',
        command = lambda : controller.show_frame(Inserir_Comanda))
        voltar_inicio_btn.place(anchor='center', relx=0.5, rely=0.95)


        pratos={'Torta de Limão':[23, '/home/stella/Downloads/torta_limao.png'], 'Sonho':[12, '/home/stella/Downloads/sonho.jpg'], 'Bolo3':[23, '/home/stella/Downloads/torta_limao.png'], 
                'Bolo4':[12, '/home/stella/Downloads/sonho.jpg'], 'Bolo5':[23, '/home/stella/Downloads/torta_limao.png'], 'Bolo6':[12, '/home/stella/Downloads/sonho.jpg'], 
                'Bolo7':[23, '/home/stella/Downloads/torta_limao.png'], 'Bolo8':[12, '/home/stella/Downloads/sonho.jpg'], 'Bolo9':[23, '/home/stella/Downloads/torta_limao.png'],
                }

 
        
        class frame_escolha(tk.Frame):
            
            def __init__(self, parent, controller):
        
                tk.Frame.__init__(self, parent)

                self.config(bg='#F6C7B3')

                frame_escolha_doces=tk.Frame(self, bg='#F6C7B3')
                frame_escolha_doces.place(relwidth=0.5, relheight=0.25, anchor='center', relx=0.5, rely=0.15)
                doces_btn=tk.Button(frame_escolha_doces, text = 'Doces', font = ('calibre',15), bg="#F8D5C6", fg='#CE724B',
                command = lambda : controller.show_frame_cardapio(frame_pratos))
                doces_btn.pack(side='bottom')
                image_doce=Image.open('/home/stella/Downloads/doces.png')
                resized_image_doce=image_doce.resize((288,162))
                bg_doce=ImageTk.PhotoImage(resized_image_doce)
                label_imagem_doce=tk.Label(frame_escolha_doces, image=bg_doce)
                label_imagem_doce.image = bg_doce
                label_imagem_doce.pack()


                frame_escolha_salgados=tk.Frame(self, bg='#F6C7B3')
                frame_escolha_salgados.place(relwidth=0.5, relheight=0.25, anchor='center', relx=0.5, rely=0.45)
                salgados_btn=tk.Button(frame_escolha_salgados, text = 'Salgados', font = ('calibre',15), bg="#F8D5C6", fg='#CE724B',
                command = lambda : controller.show_frame_cardapio(frame_pratos))
                salgados_btn.pack(side='bottom')
                image_salgado=Image.open('/home/stella/Downloads/salgados.png')
                resized_image_salgado=image_salgado.resize((288,162))
                bg_salgado=ImageTk.PhotoImage(resized_image_salgado)
                label_imagem_salgado=tk.Label(frame_escolha_salgados, image=bg_salgado)
                label_imagem_salgado.image = bg_salgado
                label_imagem_salgado.pack()

                frame_escolha_bebidas=tk.Frame(self, bg='#F6C7B3')
                frame_escolha_bebidas.place(relwidth=0.5, relheight=0.25, anchor='center', relx=0.5, rely=0.75)
                bebidas_btn=tk.Button(frame_escolha_bebidas, text = 'Bebidas', font = ('calibre',15), bg="#F8D5C6", fg='#CE724B',
                command = lambda : controller.show_frame_cardapio(frame_pratos))
                bebidas_btn.pack(side='bottom')
                image_bebidas=Image.open('/home/stella/Downloads/bebidas.png')
                resized_image_bebidas=image_bebidas.resize((288,162))
                bg_bebidas=ImageTk.PhotoImage(resized_image_bebidas)
                label_imagem_bebidas=tk.Label(frame_escolha_bebidas, image=bg_bebidas)
                label_imagem_bebidas.image = bg_bebidas
                label_imagem_bebidas.pack()

        class frame_pratos(tk.Frame):
            
            def __init__(self, parent, controller):
        
                tk.Frame.__init__(self, parent)

                nonlocal frame_pedidos

                voltar_menu_btn=tk.Button(frame_cardapio, text = 'Voltar ao menu', font = ('calibre',18), bg = '#F6C7B3', fg = '#CE724B',
                command = lambda : controller.show_frame_cardapio(frame_escolha))
                voltar_menu_btn.place(relx=0.01, rely=0.01)

                #frame_pratos=tk.Frame(frame_cardapio, bg='#F6C7B3')
                #frame_pratos.place(relwidth=1,relheight=0.9, relx=0, rely=0.1)
                
                self.config(bg='#F6C7B3')
                self.rowconfigure(0, weight=1, minsize=150)
                self.columnconfigure(0,weight=1, minsize=100)
                self.rowconfigure(1, weight=1, minsize=150)
                self.columnconfigure(1,weight=1, minsize=100)
                self.rowconfigure(2, weight=1, minsize=150)
                self.columnconfigure(2,weight=1, minsize=100)

                x_pratos=0
                y_pratos=0
                cont_pratos=0

                for prato in pratos:
                    cont_pratos+=1
                    
                    pedidos_da_comanda[prato]=0

                    frame_prato=tk.Frame(self, bg="#FFE5D9", width= 100, height=150)
                    frame_prato.grid_propagate(0)
                    frame_prato.config(width= 100, height=150)
                    frame_prato.grid(row=x_pratos, column=y_pratos)
                
                    image_prato=Image.open(pratos[prato][1])
                    resized_image=image_prato.resize((130,130))
                    bg_prato=ImageTk.PhotoImage(resized_image)
                    
                    label_imagem_prato=tk.Label(frame_prato, image=bg_prato)
                    label_imagem_prato.image = bg_prato
                    label_imagem_prato.pack()

                    label_nome_prato=tk.Label(frame_prato, text=prato, font = ('calibre',13, 'bold'), bg='#FFE5D9', fg="#CE724B" )
                    label_nome_prato.pack()

                    label_preco_prato=tk.Label(frame_prato, text='R$ '+str(pratos[prato][0]), font = ('calibre',14), bg='#FFE5D9', fg="#CE724B" )
                    label_preco_prato.pack()

                    if prato=='Torta de Limão':
                        ad_prato_btn = tk.Button (frame_prato, text='Adicionar', bg = '#F6C7B3', fg="#CE724B", font = ('calibre',14, 'bold'),
                        command = lambda : ad_prato('Torta de Limão', label_quant_prato1))
                        label_quant_prato1 = tk.Label(frame_lista_pedidos)
                    elif prato=='Sonho':
                        ad_prato_btn = tk.Button (frame_prato, text='Adicionar', bg = '#F6C7B3', fg = '#CE724B', font = ('calibre',14, 'bold'),
                        command = lambda : ad_prato('Sonho', label_quant_prato2))
                        label_quant_prato2 = tk.Label(frame_lista_pedidos)
                    elif prato=='Bolo3':
                        ad_prato_btn = tk.Button (frame_prato, text='Adicionar', bg = '#F6C7B3', fg = '#CE724B', font = ('calibre',14, 'bold'),
                        command = lambda : ad_prato('Bolo3', label_quant_prato3))
                        label_quant_prato3 = tk.Label(frame_lista_pedidos)
                    elif prato=='Bolo4':
                        ad_prato_btn = tk.Button (frame_prato, text='Adicionar', bg = '#F6C7B3', fg = '#CE724B', font = ('calibre',14, 'bold'),
                        command = lambda : ad_prato('Bolo4', label_quant_prato4))
                        label_quant_prato4 = tk.Label(frame_lista_pedidos)
                    elif prato=='Bolo5':
                        ad_prato_btn = tk.Button (frame_prato, text='Adicionar', bg = '#F6C7B3', fg = '#CE724B', font = ('calibre',14, 'bold'),
                        command = lambda : ad_prato('Bolo5', label_quant_prato5))
                        label_quant_prato5 = tk.Label(frame_lista_pedidos)
                    elif prato=='Bolo6':
                        ad_prato_btn = tk.Button (frame_prato, text='Adicionar', bg = '#F6C7B3', fg = '#CE724B', font = ('calibre',14, 'bold'),
                        command = lambda : ad_prato('Bolo6', label_quant_prato6))
                        label_quant_prato6 = tk.Label(frame_lista_pedidos)
                    elif prato=='Bolo7':
                        ad_prato_btn = tk.Button (frame_prato, text='Adicionar', bg = '#F6C7B3', fg = '#CE724B', font = ('calibre',14, 'bold'),
                        command = lambda : ad_prato('Bolo7', label_quant_prato7))
                        label_quant_prato7 = tk.Label(frame_lista_pedidos)
                    elif prato=='Bolo8':
                        ad_prato_btn = tk.Button (frame_prato, text='Adicionar', bg = '#F6C7B3', fg = '#CE724B', font = ('calibre',14, 'bold'),
                        command = lambda : ad_prato('Bolo8', label_quant_prato8))
                        label_quant_prato8 = tk.Label(frame_lista_pedidos)
                    elif prato=='Bolo9':
                        ad_prato_btn = tk.Button (frame_prato, text='Adicionar', bg = '#F6C7B3', fg = '#CE724B', font = ('calibre',14, 'bold'),
                        command = lambda : ad_prato('Bolo9', label_quant_prato9))
                        label_quant_prato9 = tk.Label(frame_lista_pedidos)
                    ad_prato_btn.pack()

                    if (cont_pratos%3==0):
                        x_pratos+=1
                    if y_pratos==2:
                        y_pratos=0
                    else:
                        y_pratos+=1
                
        dicio_frames_menu = {}
        
        for F1 in (frame_escolha, frame_pratos):
 
            frame=F1(frame_cardapio, self)
            frame.place(relwidth=1,relheight=0.9, relx=0, rely=0.08)

            dicio_frames_menu[F1] = frame

        self.show_frame_cardapio(frame_escolha)
        
        '''
        image_logo=Image.open('/home/stella/Downloads/logo.png')
        resized_image_logo=image_logo.resize((200, 200))
        bg_logo=ImageTk.PhotoImage(resized_image_logo)
        label_imagem_logo=tk.Label(frame_menu_pedidos, image=bg_logo)
        label_imagem_logo.image = bg_logo
        label_imagem_logo.place(anchor='ne', relx=0.8, rely=0.2)
        '''

    def show_frame_cardapio(self, cont):
        frame = dicio_frames_menu[cont]
        frame.tkraise()


        
# Driver Code
app = tkinterApp()
app.mainloop()