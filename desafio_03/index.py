#desafio 1: Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...) 
# escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
def pertence_fibonacci(n):
    fibonacci = [0, 1] 
    while fibonacci[-1] < n:
        proximo_numero = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_numero)

    if n in fibonacci:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
mensagem = pertence_fibonacci(numero)
print(mensagem)







#desafio 2:Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, 
# além de informar a quantidade de vezes em que ela ocorre.
string = input("Digite uma string: ")
contagem_a_minusc = 0
contagem_a_maiusc = 0

for caractere in string:   
    if caractere == 'a':
        contagem_a_minusc += 1
    elif caractere == 'A':
        contagem_a_maiusc += 1

print(f"A letra 'a' minúscula aparece {contagem_a_minusc} vez(es) na string.")
print(f"A letra 'A' maiúscula aparece {contagem_a_maiusc} vez(es) na string.")








#desafio 3: Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; 
# enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

indice = 12
soma = 0
k = 1

while k < indice:
    k = k + 1
    soma = soma + k

print(f"o resultado da variavel SOMA é {soma}")
