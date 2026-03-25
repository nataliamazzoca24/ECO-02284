"""
Programa adulto
Descrição:Este programa pergunta a idade de uma pessoa. Se a pessoa for maior de 18 anod, o programa imprime na tela "oi! Você é um adulto". Caso contrário, imprime "Oi! Você é menor de idade".
Autor: Natália
Data: 24/03/2026
Versão: 0.1.0
"""

# Alocação de memória
i = 0
texto = ""

# Entrada de dados
idade = int(input("Qual é a sua idade?"))

# Processamento de dados
if idade >= 18:
    texto = "Oi! Você é um adulto."
else:
    texto = "Oi! Você é menor de idade."

# Saída de dados
print(texto)