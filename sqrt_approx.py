# -*- coding: utf-8 -*-

import math
from ._utils import compose
from .chakravala import chakravala_terno

def sqrt_approx(n, eps):
    """
    Este método devolve um valor aproximado para a raíz quadrada de n usando 
    os valores do Python para os quadrados perfeitos e o método Chakravala
    para os não-quadrados.
    'eps' é a nossa tolerância, quantas casas decimais queremos ver correctas.
    O método devolve, sob a forma de um dicionário, a aproximação obtida, 
    o valor do Python, quantas iterações foram necessárias, o valor racional 
    da aproximação, o erro absoluto e o erro relativo
    Argumentos:
        n - int
        eps - int
    Exemplo:
        sqrt_approx(3,2)
        {'sqrt_appr': 1.7321428571428572,
         'sqrt_real': 1.7320508075688772,
         'iter': 3,
         'frac_value': '97/56',
         'abs_err_fv': 9.204957398001312e-05,
         'percent_rel_err_fv': 0.005314484631613325}
    """
    c_n = chakravala_terno(n)
    sqrta = c_n[0]/c_n[1]
    i = 1
    while sqrta - math.sqrt(n) > 10**(-eps):
        i+=1
        c_n = compose(c_n, c_n, n)
        sqrta = c_n[0]/c_n[1]
    dictio = {'sqrt_appr': sqrta, 
            'sqrt_real': math.sqrt(n),
            'iter': i, 
            'frac_value': '{}/{}'.format(c_n[0],c_n[1]), 
            'abs_err_fv': sqrta - math.sqrt(n),
            'percent_rel_err_fv': (sqrta/math.sqrt(n) - 1)*100
            }
    return dictio

def sqrt_app(n,eps):
    """
    Este método devolve um valor aproximado para a raíz quadrada de n usando
    os valores do Python para os quadrados perfeitos e o método Chakravala
    para os não-quadrados.
    'eps' é a nossa tolerância, quantas casas decimais queremos ver corretas.
    Argumentos:
        n, eps - int
    Devolve
        vals - tuple
    Exemplo:
        sqrt_app(2,4)
            >> (1.4142156862745099, '577/408')
        
    """
    vals = sqrt_approx(n,eps)['sqrt_appr'], sqrt_approx(n,eps)['frac_value']
    return vals