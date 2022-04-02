import random
from tkinter import *
from PIL import Image, ImageTk

# config janela

janela = Tk()
janela.title("")
janela.geometry("400x405")
janela.configure(background="#feffff")
janela.resizable(width=FALSE, height=FALSE)

# config frame

frame_cima = Frame(janela, width=500, height=50, bg="#3fb5a3")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=210, bg="#f0f3f5")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

l_app = Label(frame_cima, text="Acenda as Lâmpadas", anchor=NE, font="Ivy 20",
              bg="#3fb5a3", fg="#403d3d")
l_app.place(x=5, y=5)

frame_faixa = Frame(janela, width=100, height=40, bg="#3fb5a3")
frame_faixa.grid(row=2, column=0, pady=1, padx=0, sticky=NSEW)
faixa_text = Label(frame_faixa, text="Estatísticas", anchor=NE, font="Ivy 20",
                   bg="#3fb5a3", fg="#403d3d")
faixa_text.place(x=120, y=3)

frame_estatisticas = Frame(janela, width=500, height=210, bg="#f0f3f5")
frame_estatisticas.grid(row=3, column=0, pady=1, padx=0, sticky=NSEW)

l_est_1 = Label(frame_estatisticas, text="Pontuação Final:", anchor=NW, font="Ivy 18",
                bg="#f0f3f5", fg="black")
l_est_1.place(x=10, y=10)

valor_est_1 = Label(frame_estatisticas, text="0 pontos", anchor=NW, font="Ivy 18",
                    bg="#f0f3f5", fg="black")
valor_est_1.place(x=205, y=10)

l_est_2 = Label(frame_estatisticas, text="Interuptores acesos:", anchor=NW, font="Ivy 18",
                bg="#f0f3f5", fg="black")
l_est_2.place(x=10, y=60)

valor_est_2 = Label(frame_estatisticas, text="0 interuptor", anchor=NW, font="Ivy 18",
                    bg="#f0f3f5", fg="black")
valor_est_2.place(x=240, y=60)

# config images

img_medalha = Image.open("image/icon_medalha.png")
img_medalha = img_medalha.resize((55, 55))
img_medalha = ImageTk.PhotoImage(img_medalha)

l_texto = Label(frame_baixo, text="0 pontos", anchor=NW, font="Ivy 18",
                bg="#f0f3f5", fg="black")
l_texto.place(x=80, y=10)

img_bronze = Image.open("image/icon_bronze.png")
img_bronze = img_bronze.resize((50, 50))
img_bronze = ImageTk.PhotoImage(img_bronze)

img_prata = Image.open("image/icon_prata.png")
img_prata = img_prata.resize((50, 50))
img_prata = ImageTk.PhotoImage(img_prata)

img_ouro = Image.open("image/icon_ouro.png")
img_ouro = img_ouro.resize((50, 50))
img_ouro = ImageTk.PhotoImage(img_ouro)

medalha = Label(frame_baixo, image=img_medalha, bg="#f0f3f5")
medalha.place(x=20, y=0)

img_lamps_off = Image.open("image/0.png")
img_lamps_off = img_lamps_off.resize((110, 110))
img_lamps_off = ImageTk.PhotoImage(img_lamps_off)

img_lamps_on = Image.open("image/1.png")
img_lamps_on = img_lamps_on.resize((110, 110))
img_lamps_on = ImageTk.PhotoImage(img_lamps_on)

l_image_1 = Label(frame_baixo, image=img_lamps_off, bg="#f0f3f5")
l_image_1.place(x=5, y=70)

l_image_2 = Label(frame_baixo, image=img_lamps_off, bg="#f0f3f5")
l_image_2.place(x=105, y=70)

l_image_3 = Label(frame_baixo, image=img_lamps_off, bg="#f0f3f5")
l_image_3.place(x=205, y=70)

# config interuptores

global controle

x = 0


def lamps_on(l):
    global control
    global x
    lista = l
    if lista[1] == "interuptor 1":
        b_interuptor_1["state"] = "disable"
        x += 1
        if x == 1:
            valor_est_2["text"] = f"{x} interuptor"
        else:
            valor_est_2["text"] = f"{x} interuptores"
    elif lista[1] == "interuptor 2":
        b_interuptor_2["state"] = "disable"
        x += 1
        if x == 1:
            valor_est_2["text"] = f"{x} interuptor"
        else:
            valor_est_2["text"] = f"{x} interuptores"
    elif lista[1] == "interuptor 3":
        b_interuptor_3["state"] = "disable"
        x += 1
        if x == 1:
            valor_est_2["text"] = f"{x} interuptor"
        else:
            valor_est_2["text"] = f"{x} interuptores"
    elif lista[1] == "interuptor 4":
        b_interuptor_4["state"] = "disable"
        x += 1
        if x == 1:
            valor_est_2["text"] = f"{x} interuptor"
        else:
            valor_est_2["text"] = f"{x} interuptores"
    else:
        b_interuptor_5["state"] = "disable"
        x += 1
        if x == 1:
            valor_est_2["text"] = f"{x} interuptor"
        else:
            valor_est_2["text"] = f"{x} interuptores"
    print(x)

# config acender luz

    def substituir_valor(i):
        global control
        nova_lista = []

        for c in control:
            novo_valor = c.replace(i[0], i[1])
            nova_lista.append(novo_valor)

        control = nova_lista

    valor_selecionado = random.sample(lista[0], 1)[0]

    global c

    if int(valor_selecionado) == 1:
        if control[0] == "lâmpada_1":
            c = 100
            l_image_1["image"] = img_lamps_on
            medalha["image"] = img_bronze
            l_texto["text"] = f"{c} pontos"
            valor_est_1["text"] = f"{c} pontos"
            substituir_valor(["lâmpada_1", str(1)])
        else:
            if control[1] == "lâmpada_2":
                c += 200
                l_image_2["image"] = img_lamps_on
                medalha["image"] = img_prata
                l_texto["text"] = f"{c} pontos"
                valor_est_1["text"] = f"{c} pontos"
                substituir_valor(["lâmpada_2", str(2)])
            elif control[2] == "lâmpada_3":
                c += 300
                l_image_3["image"] = img_lamps_on
                medalha["image"] = img_ouro
                l_texto["text"] = f"{c} pontos"
                valor_est_1["text"] = f"{c} pontos"
                substituir_valor(["lâmpada_3", str(3)])
        print(x)

# Config pontuação final

    if int(valor_selecionado) == 0:
        if lista[1] == "interuptor 1":
            c = 0
            l_texto["text"] = f"{c} pontos"
            medalha["image"] = img_medalha
            valor_est_1["text"] = f"{c} pontos"
        elif lista[1] == "interuptor 2":
            c = 0
            l_texto["text"] = f"{c} pontos"
            medalha["image"] = img_medalha
            valor_est_1["text"] = f"{c} pontos"
        elif lista[1] == "interuptor 2":
            c = 0
            l_texto["text"] = f"{c} pontos"
            medalha["image"] = img_medalha
            valor_est_1["text"] = f"{c} pontos"
        elif lista[1] == "interuptor 3":
            c = 0
            l_texto["text"] = f"{c} pontos"
            medalha["image"] = img_medalha
            valor_est_1["text"] = f"{c} pontos"
        elif lista[1] == "interuptor 4":
            c = 0
            l_texto["text"] = f"{c} pontos"
            medalha["image"] = img_medalha
            valor_est_1["text"] = f"{c} pontos"
        else:
            c = 0
            l_texto["text"] = f"{c} pontos"
            medalha["image"] = img_medalha
            valor_est_1["text"] = f"{c} pontos"


control = ["lâmpada_1", "lâmpada_2", "lâmpada_3"]

lista = [1, 1, 0, 1, 0]

# config button

b_interuptor_1 = Button(frame_baixo, command=lambda l=[lista, "interuptor 1"]: lamps_on(l),
                        text="Interuptor 1", anchor=NW, font="Ivy 9 bold",
                        relief=RAISED, overrelief=RIDGE, bg="#403d3d", fg="#feffff")
b_interuptor_1.place(x=300, y=50)

b_interuptor_2 = Button(frame_baixo, command=lambda l=[lista, "interuptor 2"]: lamps_on(l),
                        text="Interuptor 2", anchor=NW, font="Ivy 9 bold",
                        relief=RAISED, overrelief=RIDGE, bg="#403d3d", fg="#feffff")
b_interuptor_2.place(x=300, y=80)

b_interuptor_3 = Button(frame_baixo, command=lambda l=[lista, "interuptor 3"]: lamps_on(l),
                        text="Interuptor 3", anchor=NW, font="Ivy 9 bold",
                        relief=RAISED, overrelief=RIDGE, bg="#403d3d", fg="#feffff")
b_interuptor_3.place(x=300, y=110)

b_interuptor_4 = Button(frame_baixo, command=lambda l=[lista, "interuptor 4"]: lamps_on(l),
                        text="Interuptor 4", anchor=NW, font="Ivy 9 bold",
                        relief=RAISED, overrelief=RIDGE, bg="#403d3d", fg="#feffff")
b_interuptor_4.place(x=300, y=140)

b_interuptor_5 = Button(frame_baixo, command=lambda l=[lista, "interuptor 5"]: lamps_on(l),
                        text="Interuptor 5", anchor=NW, font="Ivy 9 bold",
                        relief=RAISED, overrelief=RIDGE, bg="#403d3d", fg="#feffff")
b_interuptor_5.place(x=300, y=170)


janela.mainloop()
