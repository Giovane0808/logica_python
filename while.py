#1
'''contador = 1
while contador < 11:
      print(contador)
      contador = contador + 1'''

#2
'''contador = 10
while contador > 0:
    print(contador)
    contador = contador - 1'''

#3
'''somador = 0
#contador = 0
numero = int(input("Informe o numero:"))
while numero != 0:
    somador = somador + numero
    numero = int(input("Informe o numero:"))
print(f"A soma dos numeros é:{somador}")'''


#4
'''senha = str(input("Informe a senha:"))

while senha != "python123":
    print("SENHA INVALIDA")
    senha = str(input("Informe a senha:"))
print("SENHA CORRETA")'''


#5
'''continuar = 'sim'
#numero = int(input("Informe o numero:"))
while continuar == 'sim':
    numero = int(input("Informe o numero:"))
    for contador in range(1,11):
        #resultado = contador * numero
        print(f"{numero} X {contador} = {numero*contador}")
        contador = contador + 1
    continuar = str(input("Quer continuar?[sim/não]:"))
    while continuar != 'não' and continuar != 'sim':
      print("Resposta inválida. Digite 'sim' ou 'não'.")
      continuar = input("Quer continuar? [sim/não]: ")
print("FIM DO PROGRAMA")'''


'''Exercícios com while:
1. Contar de 1 a 10
Use while para imprimir os números de 1 a 10.

2. Contagem regressiva de 10 até 1
Use while para fazer uma contagem regressiva.

3. Somar até o usuário digitar 0
Fique pedindo números ao usuário e vá somando até ele digitar 0. Depois, mostre a soma total.

4. Validação de senha simples
Peça para o usuário digitar uma senha até que ele acerte a senha correta (ex: "python123").

5. Mostrar a tabuada de um número até o usuário querer parar
Peça um número e mostre a tabuada. Depois, pergunte se quer continuar. Repita até ele digitar “não”.'''





3. Adivinhe o número
Crie um jogo simples onde o programa escolhe um número fixo (por exemplo, 7). 
Use um while para pedir que o usuário tente adivinhar até acertar, mostrando dicas (“Tente um número maior”, “Tente um número menor”).
                                                                                
7. Repetir uma palavra até o usuário dizer “pare”
Peça uma palavra e a imprima repetidamente até o usuário digitar “pare”.