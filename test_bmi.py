import bmiCalc

def test_bmi_calc():
    bmi = bmiCalc.bmi_calc(153, 68)
    assert bmi == 23.8

def test_bmi_sort():
    sort = bmiCalc.bmi_sort(26)
    assert sort == 'overweight'
