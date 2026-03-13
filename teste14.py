#57
'''#sexo= 'M' and "F" and "S"
#sexo = str(input("Informe o sexo da pessoa:")).strip().upper()
sexo = 'M'.strip().upper()
while sexo != "M" or sexo != "F":
    sexo = str(input("Informe o sexo da pessoa:")).strip().upper()
    if sexo == "M":
        print("Está Correto")
        print(f"Seu sexo é Masculino")
    elif sexo == "F":
        print("Está Correto")
        print("Seu sexo é Feminino")
        break
    else:
        print(f"{sexo} Não é uma opção valida")'''
    





#58
'''from random import randint

total = 0

jogador = int(input("Informe o numero do jogador:"))
if jogador >= 0 and jogador <= 2:
    print("Pode Começar")
    computador = randint(0,2)
    total = total + 1
    while jogador != computador:
        print(f"O jogador escolheu o numero:{jogador}\nO computador escolheu:{computador}")
        print("Jogador errou o numero do computador")
        print("TENTANDO NOVAMENTE")
        jogador = int(input("Informe o numero do jogador:"))
        computador = randint(0,2)
        total = total + 1
    print(f"O jogador escolheu o numero:{jogador}\nO computador escolheu:{computador}")
    print("Jogador acertou o numero do computador")   
    print(f"Você teve {total} tentativas para acertar")
else:
    print("Jogada Invalida")'''







#59

'''#opção = int(input("Informe a opção escolhida:"))
#while opção == 1 or opção == 2 or opção == 3 or opção == 4:
valor1 = int(input("Informe o primeiro valor:"))
valor2 = int(input("Informe o segundo valor:"))
print(f"Os valores informados são {valor1} e {valor2}")
opção = 0

while opção != 5:
    #valor1 = int(input("Informe o primeiro valor:"))
    #valor2 = int(input("Informe o segundo valor:"))
    #print(f"Os valores informados são {valor1} e {valor2}")
    print("=============MENU==================")
    print("[1]-Somar\n[2]-Multiplicar\n[3]-Maior\n[4]-Novos Numeros\n[5]-Sair do Programa")
    opção = int(input("Informe a opção escolhida:"))

    if opção == 1:
        print(f"A soma entre {valor1} e {valor2} é igual a:{valor1 + valor2}")
    elif opção == 2:
        print(f"A multplicação entre {valor1} e {valor2} é igual a:{valor1 * valor2}")
    elif opção == 3:
        if valor1 > valor2:
            print(f"O maior valor é:{valor1}")
        elif valor2 > valor1:
            print(f"O maior valor é:{valor2}")
        else:
            print(f"{valor1} e {valor2}.Ambos os valores são iguais")
    elif opção == 4:
        valor1 = 0
        valor2 = 0
        valor1 = int(input("Informe o primeiro valor:"))
        valor2 = int(input("Informe o segundo valor:"))
        print(f"Os valores informados são {valor1} e {valor2}")
    elif opção == 5:
        print("SAIR DO PROGRAMA")
    else:
        print("Nenhuma opção escolhida\nTENTE NOVAMENTE")'''



#60

'''from math import factorial

contador = 0

numero = int(input("Informe o numero:"))

resultado = factorial(numero)

contador = numero

print(f"O fatorial de {numero}! é", end = " ")

while contador > 1:
    print(f"{contador} X", end = " ")
    contador = contador - 1
    
print(f"1 = {resultado}")


from math import factorial

contador = 0

numero = int(input("Informe o numero:"))

resultado = factorial(numero)

contador = numero

print(f"O fatorial de {numero}! é", end = " ")

for contador in range (numero,1,-1):
    print(f"{contador} X", end = " ")
    contador = contador - 1
    
print(f"1 = {resultado}")'''


#61
'''contador = 0
primeiro_termo = int(input("Informe o primeiro termo da P.A."))
razao = int(input("Informe a razão da P.A."))

decimo_termo = primeiro_termo + (10 - 1) * razao

while primeiro_termo <= decimo_termo:
    
    print(f"{primeiro_termo}", end="-")
    primeiro_termo = primeiro_termo + razao
    contador = contador + 1
print("FIM")'''

#62
'''contador = 0
primeiro_termo = int(input("Informe o primeiro termo da P.A."))
razao = int(input("Informe a razão da P.A."))

decimo_termo = primeiro_termo + (10 - 1) * razao

while primeiro_termo <= decimo_termo:
    
    print(f"{primeiro_termo}", end="-")
    primeiro_termo = primeiro_termo + razao
    contador = contador + 1
print("PAUSA\n\n")
ultimo_termo = decimo_termo
mais_termos = int(input("Quanto termos você quer mostrar?"))
while mais_termos != 0:
    #razao = int(input("Informe a razão da P.A."))
    ultimo_termo = primeiro_termo + (mais_termos - 1) * razao

    while primeiro_termo <= ultimo_termo:
                
                print(f"{primeiro_termo}", end="-")
                primeiro_termo = primeiro_termo + razao
                contador = contador + 1
    print("PAUSA\n\n")
    mais_termos = int(input("Você quer mostrar mais termos?"))
print(f"O total de termos mostrados foi {contador}")
print("FIM")'''

#63

'''numero = int(input("Informe a sequencia de fibonacci."))

primeiro_numero = 0
segundo_numero = 1

print(f"{primeiro_numero} - {segundo_numero}", end=" - ")

contador = 3

while contador <= numero:
    terceiro_numero = primeiro_numero + segundo_numero
    print(f"{terceiro_numero}", end=" - ")
    primeiro_numero = segundo_numero
    segundo_numero = terceiro_numero
    contador = contador + 1
print("FIM")'''


#64

'''somador = 0
valores = 0
numero = 0
numero = int(input("Informe o numero:"))
primeiro = numero
while numero != 999:
    valores = valores + 1
    somador = somador + numero
    numero = int(input("Informe o numero:"))
print(f"A soma dos {valores} numeros é {somador}")'''

#65

'''somador = 0
valores = 0
media = 0
maior_numero = 0
menor_numero = 0
resposta = "S"
ultimo_numero = None

while resposta == "S":
    numero = int(input("Informe o numero:"))
    
    
    if numero == ultimo_numero:
        print("Iguais! Tente novamente.")
    else:
        
        valores = valores + 1
        somador = somador + numero
        ultimo_numero = numero 
        
        if valores == 1:
            maior_numero = menor_numero = numero
        else:
            if numero > maior_numero:
                maior_numero = numero
            if numero < menor_numero:
                menor_numero = numero
    
    
    resposta = str(input("Quer continuar?[S/N] ")).strip().upper()
    while resposta != "S" and resposta != "N":
        print("ERRO! Digite apenas S ou N")
        resposta = str(input("Quer continuar?[S/N] ")).strip().upper()


if valores > 0:
    media = somador / valores
    print(f"A quantidade de numeros digitados foi:{valores}\nA media foi:{media}")
    print(f"O maior valor é:{maior_numero}\nO menor valor é:{menor_numero}")'''
