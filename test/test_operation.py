from src.math import sum,mul

def sum_test():
    assert sum(2,3)==5
    assert sum(5,6)==11
    assert sum(-5,8)==3

def mul_test():
    assert mul(2,3)==6
    assert mul(5,6)==30
    assert mul(-5,-3)==15
    assert mul(-5,3)== -15