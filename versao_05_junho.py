import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image


LARGEFONT =("Verdana", 25)


class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a container
        container = tk.Frame(self, width=700, height=700) 
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
            #frame.config()
            frame.grid(row = 0, column = 0, sticky ="nsew")
            #frame.grid_propagate(0)
        
        self.show_frame(Inserir_Comanda)
        
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        if cont==Menu_Pedidos:
            global comanda
            global num_comanda
            comanda=num_comanda.get()
            label_pedidos.config(text=('PEDIDOS DA COMANDA %s' % comanda))
        elif cont==Inserir_Comanda:
            num_comanda=tk.StringVar()
            #num_comanda.set("")
            comanda_entry.config(textvariable=num_comanda)
            
 
# first window frame startpage
 
class Inserir_Comanda(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        global comanda
        global num_comanda
        global comanda_entry
        
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


        frame_inserir_comanda=tk.Frame(self, bg='#B67233', bd=2)
        frame_inserir_comanda.config(width= 400, height=200)
        frame_inserir_comanda.place(anchor='c', relx=0.5, rely=0.5)
        frame_inserir_comanda.grid_propagate(0)
        
       
        
        
        comanda_label = tk.Label(frame_inserir_comanda, text = 'Número da comanda:', font=('calibre',20, 'bold'), fg='#FFD59A', bg='#B67233')
        comanda_label.pack(side='top')

        

        comanda_entry = tk.Entry(frame_inserir_comanda, textvariable = num_comanda, font=('calibre',20,'normal'), bg='#FFD59A')
        comanda_entry.pack(side='top')

        confirmar_btn=tk.Button(frame_inserir_comanda,text = 'Confirmar', font = ('calibre',15), bg='#FFD59A',
        command = lambda : controller.show_frame(Menu_Pedidos))
        confirmar_btn.pack(side='top')
         

 
# second window frame page1 
class Menu_Pedidos(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)

        global label_pedidos


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

        image_path="/home/stella/Downloads/cafeteria(2).png"

        bg_menu=fit_image_to_window(image_path, (700, 700))
        background_label_menu = tk.Label(self, image = bg_menu)
        background_label_menu.place(x=0, y=0, relwidth=1, relheight=1)
        background_label_menu.image = bg_menu

        self.bind('<Configure>', update_image)
        

        frame_cardapio = tk.Frame(self, bg='#F6C7B3', bd=2)
        frame_cardapio.place(relwidth=0.6, relheight=0.8, relx=0.4, rely=0.15)
        label_cardapio = tk.Label(frame_cardapio, text='CARDÁPIO', font=('calibre',20, 'bold'), bg='#F6C7B3', fg="#CE724B")
        label_cardapio.pack( side='top')

        pratos={'Torta de Limão':[23, '/home/stella/Downloads/torta_limao.png'], 'Sonho':[12, '/home/stella/Downloads/sonho.jpg']}
        for prato in pratos:
            image_prato=Image.open(pratos[prato][1])
            resized_image=image_prato.resize((100,100))
            bg_prato=ImageTk.PhotoImage(resized_image)
            frame_prato=tk.Frame(frame_cardapio, width=150, height=150, bg='white')
            frame_prato.pack()
            label_imagem_prato=tk.Label(frame_prato, image=bg_prato)
            label_imagem_prato.image = bg_prato
            label_imagem_prato.pack()
            label_nome_prato=tk.Label(frame_prato, text=prato, fg='black', bg='white')
            label_nome_prato.pack()
            label_preco_prato=tk.Label(frame_prato, text='R$ '+str(pratos[prato][0]), fg='black', bg='white')
            label_preco_prato.pack()


        frame_pedidos = tk.Frame(self, bg='#F6C7B3', bd=2)
        frame_pedidos.place(relwidth=0.35, relheight=0.8, relx=0, rely=0.15)
    
        label_pedidos = tk.Label(frame_pedidos, text=('PEDIDOS DA COMANDA' ), font=('calibre',15, 'bold'), bg='#F6C7B3', fg='#CE724B')
        label_pedidos.pack( side='top')

        voltar_btn=tk.Button(self, text = 'Voltar ao início', font = ('calibre',13), bg = '#F6C7B3', fg = '#CE724B',
        command = lambda : controller.show_frame(Inserir_Comanda))
        voltar_btn.place(relx=0.4)
        voltar_btn.pack(side='bottom')


        
# Driver Code
app = tkinterApp()
app.mainloop()