def bmi_calc(weight, height):

    metric_w = weight * 0.45
    metric_h = height * 0.025
    h_sqr = metric_h * metric_h
    bmi = metric_w / h_sqr
    bmi = round(bmi,1)

    return bmi;

def bmi_sort(bmi):

    if(bmi <= 18.5):
        sort = 'underweight'
    if(bmi > 18.5 and bmi <= 24.9):
        sort = 'normal'
    if(bmi >= 25):
        sort = 'overweight'
        
    return sort;
