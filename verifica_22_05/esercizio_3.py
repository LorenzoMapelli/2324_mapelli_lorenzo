import random

nomeFile="frasis.txt"
lista=[]
scelte=[]
giocatori=[]
montepremio=[]

def domande(nf,l):
    f=open(nf,"r")
    for i in f:
        s=i[:-1]
        frase=s.split("|")
        domanda=frase[0]
        risposta=frase[1]
        carlo=(domanda, risposta)
        l.append(carlo)
    f.close()

def numerogiocatori():
    errore=False
    while errore == False:
        azione=(input("in quanti giocano? massimo 4 minimo 2 "))
        if azione == '2' or azione == '3' or azione == '4':
            return azione 
        else:
            print("numero non adatto")

def chiedinick(gioca):
    numero=int(numerogiocatori())
    for i in range(numero):
        nome=input(f"inserire nome giocatore {i+1}")
        gioca.append(nome)
    return numero

def soldi(montepremio,n):
    for i in range(n):
        montepremio.append(0)

def casuale(l,s,n):
    for i in range(n):
        caso=random.randint(0, len(l))
        s.append(l[caso])

# def turni(s,m,g):
#     while 

domande(nomeFile, lista)
numero=chiedinick(giocatori)
soldi(montepremio,numero)
casuale(lista, scelte, numero)