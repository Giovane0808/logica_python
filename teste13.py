#46
'''from time import sleep
for contador in range(10,-1,-1):
    print(contador)
    sleep(1)
print("FELIZ ANO NOVO!!!")'''

#47
'''for contador in range(2,51,2):
    print(contador)'''

#48
'''somador = 0
valores = 0
for contador in range(1,501,2):
    numero = contador
    #if numero % 2 == 1 and contador % 3 == 0:
    if contador % 3 == 0:
       somador = somador + numero
       valores = valores + 1
print(f"A soma de todos os {valores} dos numeros impares é {somador}")'''

#49
'''numero = int(input("Informe o numero:"))
for contador in range(1,11):
    print(f"{contador} X {numero} = {contador*numero}")'''

#50
'''somador = 0
valores = 0
for contador in range(1,7):
    numero = int(input("Informe o numero:"))
    if numero % 2 == 0:
       valores = valores + 1
       somador = somador + numero
print(f"A soma dos {valores} numeros pares é {somador}")'''

#51
'''primeiro_termo = int(input("Informe o primeiro termo da P.A."))
razao = int(input("Informe a razão da P.A."))

decimo_termo = primeiro_termo + (10 - 1) * razao

for contador in range(primeiro_termo,decimo_termo + razao,razao):
    #contador = contador + razao
    print(f"{contador}")'''
#52
'''numero = int(input("Informe o numero:"))
numero_divisiveis = 0
for contador in range(1,numero + 1):
    
 if numero % contador == 0:
    print(f"Numeros divisiveis por {numero} são:{contador}")
    numero_divisiveis = numero_divisiveis + 1
 else:
    print(f"Numeros divisiveis por {numero} são:X")

#print(f"{contador}")
print(f"O numero {numero} foi dividido {numero_divisiveis} vezes")
if numero_divisiveis == 2:
  print("É PRIMO")
else:
  print("NÃO É PRIMO")'''

#53
'''frase = str(input("Informe a frase:")).strip().upper()
palavras = frase.split()
junção = ''.join(palavras)
#print(f"A frase é:{frase} e {palavras} e {junção}")
invertido = ''
for contador in range(len(junção) -1,-1,-1):
    letras = contador
    #print(junção[letras],end='')
    invertido = invertido + junção[letras]
print(f"{junção} ao contrário fica {invertido}")
if invertido == junção:
    print("É palindromo")
else:
    print("Não é palindromo")'''

#54
'''from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0
for contador in range(1,8):
    ano = contador
    ano_nascimento = int(input(f"Informe o ano de nascimento da {ano}º pessoa:"))

    idade = ano_atual - ano_nascimento 
    print(f"A idade da {contador}º pessoa é:{idade}")

    if idade < 21:
        menores = menores + 1
        print("Menor de idade")
    elif idade >= 21:
        maiores = maiores + 1
        print("Maior de idade")
print("=============================================")
print(f"O total de pessoas menores de idade são:{menores}")
print(f"O total de pessoas maiores de idade são:{maiores}")'''

    
'''if ano_atual - ano_nascimento < 21:
        menores = menores + numero
        print(f"Os menores de idade são:{menores}")
    elif ano_atual - ano_nascimento >= 21:
        maiores = maiores + numero
        print(f"Os maiores de idade são:{maiores}")  
    else:
        print(f"ERRO")'''

#55
'''maior = 0
menor = 0
for contador in range(1,6):
    peso = contador
    peso = float(input(f"Informe o peso da {contador}º pessoa:"))
    print(f"O peso da {contador}º pessoa é:{peso}")

    if contador == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
           maior = peso
        if peso < menor:
           menor = peso
        
print("=============================================")
print(f"O maior peso é:{maior}")
print(f"O menor peso é:{menor}")

#maior = max(peso)
#menor = min(peso)

#print(f"Maior valor {maior}")
#print(f"Menor valor {menor}")'''

#56
'''somador_idade = 0
media = 0
idade_homem_maior = 0
nome_homem_velho = ''
total_mulher = 0
for contador in range(1,5):
    pessoa = contador
    nome = str(input(f"Informe o nome da {pessoa}º pessoa:")).strip()
    idade = int(input(f"Informe a idade da {pessoa}º pessoa:"))
    sexo = str(input(f"Informe o sexo da {pessoa}º pessoa:")).strip().upper()
    
    print(f"O Nome da {contador}º pessoa é:{nome}")
    print(f"A idade da {contador}º pessoa é:{idade}")
    print(f"O Nome da {contador}º pessoa é:{sexo}")

    if pessoa == 1 and sexo == "M":
       idade_homem_maior = idade
       nome_homem_velho = nome
    if sexo == "M" and idade > idade_homem_maior:
        idade_homem_maior = idade
        nome_homem_velho = nome
    if sexo == "F" and idade < 20:
        total_mulher = total_mulher + 1


    somador_idade = somador_idade + idade
media = somador_idade / pessoa
print(f"Media:{media}\nO homem mais velho {idade_homem_maior} e se chama {nome_homem_velho}\nNo total tem {total_mulher} mulheres com menos de 20 anos de idade")'''



