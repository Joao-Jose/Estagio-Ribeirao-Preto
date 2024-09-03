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
