def saudacao (horario):
    if not (0 <= horario <= 23):
        raise ValueError("Horário deve ser um número entre 0 e 23.")
    elif horario < 12:
        return "Bom dia!"
    elif horario < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"
    
def criar_desconto(preco, percentual):
    if percentual <= 0 or percentual > 100:
        raise ValueError("Percentual deve ser um número entre 0 e 100.")
    else:
        desconto = preco * (percentual / 100)
        return preco - desconto
    

# def convert_array_str_to_int(array_str):
#     try:
#         return [int(x) for x in array_str]
#     except ValueError:
#         raise ValueError("Um ou mais elementos da string não são números inteiros válidos.")
    

# def verifica_se_array_inteiro(array):
#     if not all(isinstance(x, int) for x in array):
#         raise ValueError("Todos os elementos do array devem ser números inteiros.")
#     return "Todos os numeros foram convertidos para inteiro com sucesso!"

if __name__ == "__main__":
    horario = int(input("Digite a hora atual (0-23): "))
    print(saudacao(horario))

    # telefones = ["1234567890", "0987654321", "5555555555"]

    # array_inteiros = convert_array_str_to_int(telefones)
    # print("Array de inteiros:", array_inteiros)
    # print("Verificação de array de inteiros:", verifica_se_array_inteiro(array_inteiros))