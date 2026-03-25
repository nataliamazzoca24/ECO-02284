"""
Programa adulto
Descrição:Este programa pergunta a idade de uma pessoa. Se a pessoa for maior de 18 anod, o programa imprime na tela "oi! Você é um adulto"
Autor: Natália
Data: 24/03/2026
Versão: 0.0.1
"""

# Alocação de memória
i = 0
texto = ""

# Entrada de dados
idade = int(input("Qual é a sua idade?"))

# Processamento de dados
if idade >= 18:
   texto = "Oi! Você é um adulto."

# Saída de dados
print(texto)