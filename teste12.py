#36
'''valor_casa = float(input("Informe o valor da casa:"))
salario_mensal = float(input("Informe seu salario por mês:"))
anos = int(input("Informe por quantos anos será pago a casa:"))

pagamento_mensal = valor_casa / (anos * 12)
porcentagem = (30/100) * salario_mensal

print(f"Valor da casa:{valor_casa}\nSalario:{salario_mensal}\nAnos de pagamento:{anos}\nPagamento mensal:{pagamento_mensal}\nPorcentagem:{porcentagem}")
if pagamento_mensal <= porcentagem:
    print("EMPRÉSTIMO APROVADO")
else:
    print("EMPRÉSTIMO NEGADO")'''



#37
'''numero = int(input("Informe o numero:"))
opção = int(input("Informe a opção:"))

if opção == 1:
    binario = bin(numero)
    print(f"O numero é {numero}\nE seu binario é {binario[2::]}")
    
elif opção == 2:
    octal = oct(numero)
    print(f"O numero é {numero}\nE seu binario é {octal[2::]}")

elif opção == 3:
    hexa = hex(numero)
    print(f"O numero é {numero}\nE seu binario é {hexa[2::]}")

else:
    print(f"O numero é {numero}\nMas não escolheu nenhuma opção")'''


'''numero = int(input("Informe o numero:"))
opção = int(input("Informe a opção:"))

print(f"O numero é {numero}")

if opção == 1:
    binario = bin(numero)
    print(f"E seu binario é {binario[2::]}")
    
elif opção == 2:
    octal = oct(numero)
    print(f"E seu binario é {octal[2::]}")

elif opção == 3:
    hexa = hex(numero)
    print(f"E seu binario é {hexa[2::]}")

else:
    print(f"Mas não escolheu nenhuma opção valida")'''




#38
'''primeiro_valor = int(input("Informe o primeiro numero:"))
segundo_valor = int(input("Informe o segundo numero:"))

print(f"Primeiro Valor = {primeiro_valor}\nSegundo Valor = {segundo_valor}")

if primeiro_valor > segundo_valor:
    print("O primeiro valor é maior")
elif segundo_valor > primeiro_valor:
    print("O segundo valor é maior")
else:
    print("Valores Iguais")'''

#39
'''from datetime import date

ano_nascimento = int(input("Informe o seu ano de nascimento:"))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

if idade == 18:
    print(f"Você tem {idade} anos de idade, hora de se alistar nesse ano de {ano_atual}")
elif idade < 18:
    idade_alistamento = 18 - idade
    print(f"Você tem {idade} anos de idade\nFaltam {idade_alistamento} anos para se alistar no ano de {ano_atual + idade_alistamento}")
elif idade > 18:
    idade_alistamento = idade - 18
    print(f"Você tem {idade} anos de idade\nDeveria ter se alistado a {idade_alistamento} anos atrás no ano de {ano_atual - idade_alistamento}")
else:
    print("ERRO")'''

#40
'''nota1 = float(input("Informe a primeira nota do aluno:"))
nota2 = float(input("Informe a segunda nota do aluno:"))

media = (nota1 + nota2) / 2

print(f"A sua média é:{media}")

if media >= 7:
    print(f"APROVADO")
elif media >= 5 and media < 7:
    print(f"RECUPERAÇÃO")
else:
    print(f"REPROVADO")'''

#41
'''from datetime import date

ano_nascimento = int(input("Informe o ano de nascimento:"))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento
print(f"Sua idade é:{idade}")

if idade <= 9:
    print(f"MIRIM")
elif idade >= 10 and idade <= 14:
    print(f"INFANTIL")
elif idade >= 15 and idade <= 19:
    print(f"JUNIOR")
elif idade >= 20 and idade <= 25:
    print(f"SÊNIOR")
else:
    print(f"MASTER")'''

#42
'''reta1 = float(input("Informe o tamanho da primeira reta:"))
reta2 = float(input("Informe o tamanho da segunda reta:"))
reta3 = float(input("Informe o tamanho da terceira reta:"))

print(f"Reta 1:{reta1}\nReta 2:{reta2}\nReta 3:{reta3}")

if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta3 + reta1) > reta2:
 print("Sim, as retas podem formar um triangulo")
 if reta1 == reta2 and reta1 == reta3 and reta2 == reta3:
    print("Equilátero")
 if reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
    print("Escaleno")
 if reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1:
    print("Isósceles") 
else:
    print("Não, as retas não podem formar um triangulo")'''

#43
'''peso = float(input("Informe seu peso:"))
altura = float(input("Informe sua altura:"))

imc = peso / (altura * altura)
print(f"IMC:{imc}")

if imc < 18.5:
  print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
  print("Peso ideal")
elif imc >= 25 and imc < 30:
  print("Sobrepeso")
elif imc >= 30 and imc < 40:
  print("Obesidade")
else:
  print("Obesidade mórbida")'''

#44
'''preço_produto = float(input("Informe o preço do produto:"))
opção = int(input("Informe a opção de pagamento:"))
print(f"Preço:{preço_produto}\nOpção Escolhida:{opção}")

if opção == 1:
    print(f"R${preço_produto - (preço_produto * 10/100)}")
elif opção == 2:
    print(f"R${preço_produto - (preço_produto * 5/100)}")
elif opção == 3:
    print(f"R${preço_produto}")
    print(f"Parcelado em 2x de R${preço_produto/2}")
elif opção == 4:
    parcela = int(input("Informe quantas parcelas:"))
    juro = preço_produto + (preço_produto * 20 / 100)
    print(f"R${juro}\nCom parcelas de {juro/parcela}")
else:
    print(f"Opção invalida\nVocê pagará R${preço_produto}")'''

#45
from random import randint
from time import sleep
jokenpo = ["tesoura","papel","pedra"]
jogador = int(input("[0]-tesoura\n[1]-papel\n[2]-pedra\nInforme a mão:"))


'''if jogador not in[0,1,2]:
    print("ERRO")

else:
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    
    computador = randint(0,2)
    
    print(f"Jogador jogou={jokenpo[jogador]}\nComputador jogou={jokenpo[computador]}")

    if jogador == 0 and computador == 0 or jogador == 1 and computador == 1 or jogador == 2 and computador == 2:
        print("Empate")
    elif jogador == 0 and computador == 1 or jogador == 1 and computador == 2 or jogador == 2 and computador == 0:
        print("Jogador venceu")
    elif computador == 0 and jogador == 1 or computador == 1 and jogador == 2 or computador == 2 and jogador == 0:
        print("Computador venceu")'''

    






'''x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)'''

'''from random import randint
jokenpo = ("tesoura","papel","pedra")
computador = randint(0,2)
print(f"O computador escolheu {jokenpo[computador]}")'''

