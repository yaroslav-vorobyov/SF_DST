from factorial import factorial as fct

def sin(x):
    sin = 1 - (x**2/fct(2)) + (x**4/fct(4)) - (x**6/fct(6)) + (x**8/fct(8)) - (x**10/fct(10))
    return round(sin, 5)