
from tkinter import *
from tkinter import Label

import tk

Tk()

valor = float
resultado = float


def feminino():
    genero = 62
    global valor
    valor += genero


def masculino():
    genero2 = 37
    global valor
    valor += genero2


def primeiro_grau():
    genetica = 52
    global valor
    valor += genetica


def segundo_grau():
    genetica1 = 40
    global valor
    valor += genetica1


def terceiro_grau():
    genetica2 = 7
    global valor
    valor += genetica2


def pri_seg():
    genetica3 = 92
    global valor
    valor += genetica3


def pri_ter():
    genetica4 = 59
    global valor
    valor += genetica4


def seg_ter():
    genetica5 = 47
    global valor
    valor += genetica5


def todos():
    genetica6 = 99
    global valor
    valor += genetica6


def peso_ideal():
    peso = 47
    global valor
    valor += peso


def abaixo_do_peso():
    peso2 = 43
    global valor
    valor += peso2


def acima_do_peso():
    peso3 = 43
    global valor
    valor += peso3


def obesidade():
    peso4 = 3
    global valor
    valor += peso4


def pratico():
    exercicio = 17
    global valor
    valor += exercicio


def sedentario():
    nao = 58
    global valor
    valor += nao


def salsicha():
    como = 13
    global valor
    valor += como


def salgadinho():
    como2 = 15
    global valor
    valor += como2


def linguiça():
    como3 = 24
    global valor
    valor += como3


def miojo():
    como4 = 13
    global valor
    valor += como4


def mortadela():
    como5 = 16
    global valor
    valor += como5


def pizza():
    como6 = 16
    global valor
    valor += como6


def meno_salario():
    recebo = 24
    global valor
    valor += recebo


def um_salario():
    recebo2 = 58
    global valor
    valor += recebo2


def mais_salario():
    recebo3 = 16
    global valor
    valor += recebo3


def calcula():
    global valor
    global resultado
    resultado = valor / 6
    texto = 'Você tem', resultado, '% chances de ser hipertenso'
    print(texto)



    texto_principal["text"] = texto

    valor = 0
    resultado = 0




def delete():
    i = 0




while (True):
    valor = 0
    resultado = 0



    janela = Tk()

    janela.geometry("1050x1000")
    janela.title("Sistema de probabilidade")





    texto = Label(janela, text="Informe seu gênero biológico", font=("Helvica", "10"))
    texto.grid(column=0, row=1, padx=5, pady=5, columnspan=2)

    botao = Button(janela, text="Feminino", command=feminino, bg="darkred", height="1", fg="white", width=15, border="4", font=("Helvica", "10", "italic", "bold"))
    botao.grid(column=0, row=2, padx=5, pady=5)
    ok = Button(janela, text="Masculino", command=masculino, bg="darkred", fg="white", height="1", width=15, border="4", font=("Helvica", "10","italic", "bold"))
    ok.grid(column=1, row=2, padx=5, pady=5)

    texto2 = Label(janela, text="Informe se há parentes hipertenso em sua familia", font=("Helvica", "10"))
    texto2.grid(column=0, row=3, padx=5, pady=5, columnspan=2)
    click = Button(janela, text="1º grau", command=primeiro_grau, bg="darkred",  height="1", fg="white", width=15, border="4", font=("Helvica", "10", "italic","bold"))
    click.grid(column=0, row=4, padx=5, pady=5)
    jj = Button(janela, text="2º grau", command=segundo_grau, bg="darkred",  height="1", fg="white", width=15, border="4", font=("Helvica", "10", "italic", "bold"))
    jj.grid(column=0, row=5, padx=5, pady=5)
    sos = Button(janela, text="3º grau", command=terceiro_grau, bg="darkred", height="1", fg="white", width=15, border="4", font=("Helvica", "10","italic", "bold"))
    sos.grid(column=0, row=6, padx=5, pady=5)
    help = Button(janela, text="1º e 2º grau", command=pri_seg, bg="darkred",  height="1", fg="white", width=15, border="4", font=("Helvica", "10","italic", "bold"))
    help.grid(column=1, row=4, padx=5, pady=5)
    gri = Button(janela, text="1º e 3º grau", command=pri_ter, bg="darkred",  height="1", fg="white", width=15, border="4", font=("Helvica", "10","italic", "bold"))
    gri.grid(column=1, row=5, padx=5, pady=5)
    gro = Button(janela, text="2º e 3º grau", command=seg_ter, bg="darkred", fg="white", width=15, border="4", font=("Helvica", "10", "bold"))
    gro.grid(column=1, row=6, padx=5, pady=5)




    texto3 = Label(janela, text="Informe seu porte físico", font=("Helvica", "10"))
    texto3.grid(column=0, row=8, padx=5, pady=5, columnspan=4)
    ta = Button(janela, text="Peso ideal", command=peso_ideal, bg="darkred", height="1", fg="white", width=15, border="4", font=("Helvica", "10","italic", "bold"))
    ta.grid(column=0, row=9, padx=5, pady=5)
    pp = Button(janela, text="Acima do peso", command=acima_do_peso, bg="darkred",  height="1",fg="white", width=15, border="4", font=("Helvica", "10","italic", "bold"))
    pp.grid(column=1, row=9, padx=5, pady=5)
    soro = Button(janela, text="Abaixo do peso", command=abaixo_do_peso, bg="darkred",  height="1", fg="white", width=15, border="4", font=("Helvica", "10","italic", "bold"))
    soro.grid(column=0, row=10, padx=5, pady=5)
    oi = Button(janela, text="Obesidade", command=obesidade, bg="darkred", fg="white",  height="1",width=15, border="4", font=("Helvica", "10","italic", "bold"))
    oi.grid(column=1, row=10, padx=5, pady=5)

    texto4 = Label(janela, text="Você costuma praticar exercicios físicos ou é sedentário?", font=("Helvica", "10"))
    texto4.grid(column=0, row=11, padx=5, pady=5, columnspan=2)
    pratics = Button(janela, text="Pratico", command=pratico, bg="darkred", fg="white", height="1", width=15, border="4", font=("Helvica", "10", "italic", "bold"))
    pratics.grid(column=0, row=12, padx=5, pady=5)
    no = Button(janela, text="Sedentario", command=sedentario, bg="darkred", fg="white",  height="1",width=15, border="4", font=("Helvica", "10", "italic", "bold"))
    no.grid(column=1, row=12, padx=5, pady=5)

    text5 = Label(janela, text="Qual dos seguintes alimentos você mais consome?", height="1", font=("Helvica", "10"))
    text5.grid(column=0, row=14, padx=5, pady=5, columnspan=2)
    sal = Button(janela, text="Salsicha", command=salsicha, bg="darkred", fg="white", height="1", width=15, border="4", font=("Helvica", "10", "italic", "bold"))
    sal.grid(column=0, row=15, padx=5, pady=5)
    ga = Button(janela, text="Salgadinho", command=salgadinho, bg="darkred", fg="white", height="1", width=15, border="4", font=("Helvica", "10", "italic", "bold"))
    ga.grid(column=1, row=15, padx=5, pady=5)
    li = Button(janela, text="Linguiça", command=linguiça, bg="darkred", fg="white", height="1", width=15, border="4", font=("Helvica", "10", "italic", "bold"))
    li.grid(column=0, row=16, padx=5, pady=5)
    mi = Button(janela, text="Miojo", command=miojo, bg="darkred", fg="white", width=15, height="1", border="4", font=("Helvica", "10", "italic", "bold"))
    mi.grid(column=1, row=16, padx=5, pady=5)
    tadela = Button(janela, text="Mortadela", command=mortadela, bg="darkred", fg="white", height="1", width=15, border="4", font=("Helvica", "10", "italic", "bold"))
    tadela.grid(column=0, row=17, padx=5, pady=5)
    pii = Button(janela, text="Pizza", command=pizza, bg="darkred", fg="white", width=15, height="1", border="4", font=("Helvica", "10", "italic", "bold"))
    pii.grid(column=1, row=17, padx=5, pady=5)

    text6 = Label(janela, text="Informe sua renda salarial", font=("Helvica", "10"))
    text6.grid(column=0, row=18, padx=5, pady=5, columnspan=3)
    pobre = Button(janela, text="Menor que 1 salário", command=meno_salario, bg="darkred", fg="white", height="1", width=15, border="4", font=("Helvica", "10", "italic", "bold"))
    pobre.grid(column=0, row=19, padx=5, pady=5)
    medio = Button(janela, text="1 salário", command=um_salario, bg="darkred", fg="white",  height="1", width=15, border="4", font=("Helvica", "10", "italic", "bold"))
    medio.grid(column=0, row=20, padx=5, pady=5)
    rico = Button(janela, text="Maior que 1 salário", command=mais_salario, bg="darkred", fg="white", height="1", width=15, border="4", font=("Helvica", "10", "italic", "bold"))
    rico.grid(column=1, row=19, padx=5, pady=5)

    text7 = Button(janela, text="Calcular", command=calcula, bg="darkred", fg="white", width=15, height="1", border="4",  font=("Helvica", "10", "bold"))
    text7.grid(column=0, row=22, padx=5, pady=5)





    texto_principal: Label = Label(janela, text="")
    texto_principal.grid(column=0, row=23, columnspan=2)
    janela.mainloop()

