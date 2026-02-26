from app.functions import *

def test_saudacao_bom_dia():
    assert saudacao(8) == "Bom dia!"

def test_saudacao_boa_tarde():
    assert saudacao(15) == "Boa tarde!"

def test_saudacao_boa_noite():
    assert saudacao(20) == "Boa noite!"

def test_saudacao_horario_invalido():
    try:
        saudacao(25)
        assert False, "Deveria ter lançado uma exceção de horário inválido"
    except ValueError:
        pass  # Exceção esperada, teste passa


def test_criar_desconto_valido():
    assert criar_desconto(100, 20) == 80

def test_criar_desconto_percentual_invalido():
    try:
        criar_desconto(100, 150)
        assert False, "Deveria ter lançado uma exceção de percentual inválido"
    except ValueError:
        pass  # Exceção esperada, teste passa