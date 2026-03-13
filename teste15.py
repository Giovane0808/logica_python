#66

'''somador = 0
contador = 0
numero = 0

while True:
    numero = int(input(f"Informe o {contador+1}º numero:"))
    if numero == 999:
        break
    contador = contador + 1
    somador = somador + numero
    #numero = int(input("Informe o numero:"))
print(f"A soma dos {contador} numeros é {somador}")'''




#67

contador = 1

while True:
    numero = int(input(f"Informe o {contador}º numero da tabuada:"))
    if numero < 0:
     print("Terminado")
     break
    print(f"==========TABUADA DE {numero}==========")
    contador_tabuada = 1
    while contador_tabuada <= 10:
     print(f"{contador_tabuada} X {numero} = {contador_tabuada*numero}")
     contador_tabuada = contador_tabuada + 1
    contador = contador + 1



'''contagem = 0
while True:
    numero = int(input(f"Informe o {contagem+1}º numero da tabuada:"))
    if numero < 0:
         print("Fim Do Programa")
         break
    print(f"Tabuda de {numero}:")
    for contador in range(1,11):
         print(f"{numero} X {contador} = {numero*contador}")
    print("====================")
    contagem = contagem + 1'''