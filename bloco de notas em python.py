import tkinter


def NewFile():
    #Deleta o arquivo escrito do inicio até o fim.
    text.delete(1.0, 'end')


def Save():
    #Salva o texto do ínicio ao fim.
    conteiner = text.get(1.0, 'end')
    #Abre o arquivo e permite a escrita, com o 'w'.
    file = open('principal.py', 'w')
    file.write(conteiner)
    file.close()


def Open():
    #Abrir documento para leitura.
    file = open('principal.py', 'r')
    container = file.read()
    file = text.insert(1.0, container)


def Update_Font():
    #Obtém a seleção do tamanho da fonte.
    size = spin_size.get()
    font = spin_type_font.get()
    text.config(font='{} {}'.format(font, size))


#Criando Janela
window = tkinter.Tk()

#Altera o título da Janela.
window.title('NotePad Jr')

#Definindo width = largura, heigth = altura com minsize
"""window.minsize(width=1200, height=650)"""

#Definindo propriedades de altura e largura da janela com geometry
#Ela é totalmente redimensionável, sem limites diferente do método minsize.
window.geometry('1200x650')

#Cria barra de frame, ou menu, foi definido a altura.
frame = tkinter.Frame(height=30)

#Organiza o frame, e o atributo dentro do método frame, torna o frame responsivo.
frame.pack(fill='x')

#Menu de fontes
font_text = tkinter.Label(frame, text=' Font: ')

#Colocar a opção de fonte, no side = lado = left = esquerdo
font_text.pack(side='left')

#Criando menu de opções de fonte - SpinBox
spin_type_font = tkinter.Spinbox(frame, values=['Alef', 'Algerian'])
spin_type_font.pack(side='left', padx=8)

#SpinBox - Menu para armazenar tamanho de fonte.
spin_font_size = tkinter.Label(frame, text=' Size Font: ')
spin_font_size.pack(side='left')


spin_size = tkinter.Spinbox(frame, from_=0, to=60)
spin_size.pack(side='left')


#Criando Botão para atualizar tamanho da fonte, e atualizar tipo de fonte.
#O primeiro parâmetro, sempre é onde eu quero inserir o objeto.
button_update = tkinter.Button(frame,text='UP', command=Update_Font)
button_update.pack(side='left', padx=25)


#Definindo fonte, tipo de fonte, e tamanho de fonte dentro da Janela.
text = tkinter.Text(window, font='Arial 20 bold', width=1200, height=650)

#Colocando o texto dentro da nossa janela.
#O método Pack, tem a função de organizar os nossos widgets.
text.pack()

#Configurando Menu da Janela
menu = tkinter.Menu(window)
window.config(menu=menu)

#Adicionando Ação no menu
#teareff tira a opção de movimentar a janela para fora do menu.
file_menu = tkinter.Menu(menu, tearoff=0)

#Adicionando SubOpções na Opção principal File.
file_menu.add_command(label='Open File', command=Open)
file_menu.add_command(label='New', command=NewFile)
file_menu.add_command(label='Save', command=Save)
file_menu.add_command(label='Save as...')
#O comando exite ao ser acionado, fecha a Janela.
file_menu.add_command(label='Exit', command=window.quit)

#Adicionando Opção Principal na Janela - File
#O método cascade abre um leque de opções.
menu.add_cascade(label='File', menu=file_menu)


#Loop que mantém a janela aberta
window.mainloop()


