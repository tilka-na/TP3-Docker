from app.calculator import addition, multi

def test_addition():
    assert addition(1, 2) == 3
    assert addition(1.5, 2.5) == 4.0
    assert addition(-1, 1) == 0

def test_multi():
    assert multi(2, 3) == 6
    assert multi(2.5, 4) == 10.0
    assert multi(-2, 5) == -10