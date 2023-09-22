from main import add,sub, mul

#Test #1
def test_add():
    assert 0 == add(0,0)
    assert -1 == add(1,-2)
    
def test_sub():
    assert 0 == sub(1,1)
    assert 5 == sub(6,1)
    
def test_mult():
    assert 100 == mul(10,10)
    assert 20 == mul(5,4)