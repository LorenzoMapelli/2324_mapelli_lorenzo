lista=[]
f = open("gusti1.txt","r")
for i in f:
    lista.append(i.strip())
print(lista)

f.close