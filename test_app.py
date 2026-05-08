from app import add, substract

def test_add():
    assert add(2, 3) == 5

def test_substract():
    assert substract(3, 2) == 1
