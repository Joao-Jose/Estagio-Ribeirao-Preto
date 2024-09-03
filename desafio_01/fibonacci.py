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
