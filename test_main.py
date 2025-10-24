from main import sumar

def test_sumar():
    assert sumar(2, 3) == 5
def test_sumar_con_negativos():
    assert sumar(-5, -2) == -7