#1
'''for contador in range(1,11):
    print(contador)'''

#2
'''for contador in range(1,11):
    resultado = contador * 5
    print("5 X ", contador ,"=", resultado)
    contador = contador + 1'''

#3
'''somador = 0
for contador in range(1,101):
    print(contador)
    somador = somador + contador
    contador = contador + 1
print(f"A soma dos numeros é:{somador}")'''

#4
'''for contador in range(1,21):
    if contador % 2 == 0:
        print(contador)
    elif contador % 2 == 1:
        print(end="")'''

'''for contador in range(1,21):
    if contador % 2 == 0:
        print(contador)'''
    
'''for contador in range(2,21,2):
    print(contador)'''
   

#5
'''contador = 1
palavra = str(input("Informe a palavra:"))

for letra in palavra:
    print(f"A {contador}ª letra da palavra é:{letra}")
    contador = contador + 1'''

'''Exercícios com for:
1. Contar de 1 a 10
Use um for para imprimir os números de 1 a 10.

2. Tabuada do 5
Mostre a tabuada do 5 usando um laço for.

3. Somar os números de 1 a 100
Use for para somar todos os números de 1 a 100.

4. Mostrar os números pares de 1 a 20
Use for para mostrar apenas os números pares de 1 a 20.

5. Mostrar cada letra de uma palavra
Peça para o usuário digitar uma palavra e use for para mostrar cada letra separadamente.'''

'''1. Contar e mostrar só os números ímpares de 1 a 30
Use um for para imprimir só os números ímpares entre 1 e 30.

2. Calcular o fatorial de um número
Peça para o usuário digitar um número inteiro positivo e use um for para calcular o fatorial dele (exemplo: 5! = 5×4×3×2×1 = 120).
    
4. Contar vogais em uma palavra
Peça para o usuário digitar uma palavra e use um for para contar quantas vogais (a, e, i, o, u) ela possui.

5. Mostrar uma sequência de Fibonacci
Peça um número n e mostre os primeiros n números da sequência de Fibonacci usando um loop for ou while.
(A sequência começa com 0, 1, 1, 2, 3, 5, 8...)

6. Tabuada de qualquer número (com validação)
Peça um número ao usuário e imprima a tabuada de 1 a 10 dele. Se o usuário digitar algo inválido (não numérico), peça de novo.'''

#1
'''for contador in range(1,31,2):
    print(contador)'''

#2
'''valor = int(input("Informe o valor:"))
for contador in range(valor,1):
    print(valor)'''

def calcular_fatorial(numero):
  resultado = 1
  # Verifica se o número é negativo
  if numero < 0:
    return "Fatorial não definido para números negativos"
  # Caso base para 0 e 1
  elif numero == 0 or numero == 1:
    return 1
  # Loop for para calcular o fatorial
  else:
    for i in range(1, numero + 1):
      resultado *= i
    return resultado

# Exemplo de uso
num = 5
print(f"O fatorial de {num} é {calcular_fatorial(num)}")