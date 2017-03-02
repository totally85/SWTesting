#testing retirement
import retirement

def test_retirement():
    result = retirement.retirement(0,100,0.02,6)
    assert result == 3

def test_savings_not_met():
    result = retirement.retirement(10,0,0.02,6)
    assert result == 100

