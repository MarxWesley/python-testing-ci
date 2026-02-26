from  app.calculadora import somar, subtrair, multiplicar, dividir

def test_soma():
    assert somar(2, 3) == 5

def test_subtracao():
    assert subtrair(5, 3) == 2

def test_multiplicacao():
    assert multiplicar(2, 3) == 6

def test_divisao():
    assert dividir(6, 2) == 3

def test_divisao_por_zero():
    try:
        dividir(6, 0)
        assert False, "Deveria ter lançado uma exceção de divisão por zero"
    except ZeroDivisionError:
        pass  # Exceção esperada, teste passa