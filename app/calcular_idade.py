from datetime import date

def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade

# Exemplo de uso
input_ano_nascimento = int(input("Digite o ano de nascimento: "))

calcular_idade_resultado = calcular_idade(input_ano_nascimento)
print(f"Sua idade é: {calcular_idade_resultado} anos.")