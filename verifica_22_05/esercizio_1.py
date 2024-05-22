import os

lista=[]
def menu():
    print("1) aggiungere un nuovo oggetto alla lista")
    print("2) eliminare uno specifico oggetto dalla lista")
    print("3) visualizzare l'elenco degli oggetti presenti nella lista")
    print("4) salvare l'elenco su file")
    print("5) caricare da file un elenco già fatto")
    print("0)esci") 

def scelta():
    errore=False
    while errore == False:
        azione=(input("cosa vuoi fare? "))
        if azione == '1' or azione == '2' or azione == '3' or azione == '4' or azione == '5' or azione == '0':
            return azione 
        else:
            print("azione non permessa")

def controllonome():
    errore=False
    while errore == False:
        nome=input("inserire il nome ")
        if (nome.isalpha())==False or len(nome)<3:
            errore=False
            print("nome non accettato ")
        else:
            return nome

def aggiungi(l):
    nome=controllonome()
    l.append(nome)

def elimina(l):
    elimina=controllonome()
    posizione=0
    for i in range(len(l)):
        if l[i] == elimina:
            posizione=l[i]
    l.pop(posizione)

def visualizza(l):
    for i in range((len(l))):
        print(f"{i}) {l[i]}")

def salva(l):
    try:
        nome=input("inserire il nome del file senza l'estensione")
        nome = nome +".myl"
        f=open("lista.myl","w")
        for i in range(len(l)):
            f.write(l[i] + "/n")           
        f.close()
    except:
        print("file non esistente")


# def carica():


continua=True
while continua == True:
    menu()
    azione=scelta()
    match azione:
        case '1':
            aggiungi(lista)
            continua=True
        case '2':
            elimina(lista)
            continua=True
        case '3':
            visualizza(lista)
            continua=True
        case '4':
            salva(lista)
            continua=True
        # case '5':

        case '0':
            quit()