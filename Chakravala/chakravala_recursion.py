# -*- coding: utf-8 -*-
"""
Esta á uma nova implementação do algoritmo Chakravala para resolução de 
equações x^2 - Dy^2 = 1 com soluções inteiras. Esta implementação usa recursão.
"""

from math import sqrt
from _utils import m_method, compose

def _chak_recu(a,b,N,i=2):
    """
    """
    #inicialização do primeiro valor
    k = a**2 - N*b**2
    #composição de ternos
    m = m_method(a,b,k,N)
    results = (a,b,k)
    brahma = (m, 1, m**2 - N)
    w = compose(results, brahma, N)
    #diminuição do valor absoluto das soluções
    a_ = int(w[0]/abs(k))
    b_ = int(w[1]/abs(k))
    k_ = int(w[2]/k**2)
    #Solução
    dictio = {'solution_x': a_,
              'solution_y': b_,
              'iterations': i}
    # Casos especiais que terminam a realização de contas demoradas.
    if k_ == 1:
        return dictio
    elif k_ == -1:
        w = compose(w, w, N)
        dictio = {'solution_x': w[0],
                'solution_y': w[1],
                'iterations' : i}
        return dictio
    elif k_ == 2:
        w = compose(w, w, N)
        w = [int(w[0]/2), int(w[1]/2), 1]
        dictio = {'solution_x': w[0],
                'solution_y': w[1],
                'iterations' : i}
        return dictio
    # Se não obtivermos nenhum dos valores anteriores, repetimos o cálculo
    else:
        ans = _chak_recu(a_,b_,N,i=i+1)
    return ans


def chakravala_rec(n):
    """
    Uma nova implementação do algoritmo da chakravala para implementar recursão
    """
    #Estas são as excepções para as quais temos de estar preparados
    if n < 0:
        raise ValueError("""Foi usado o número {}. Para este cálculo, O
                         número deve ser positivo""")
    if not isinstance(n, int):
        raise ValueError("""Foi usado o número {}. Para este cálculo, 
                         o parâmetro deve ser inteiro""")
    if math.sqrt(n).is_integer():
        raise ValueError("""Foi usado o número {}. Para este cálculo, o 
                         parâmetro não pode ser um quadrado perfeito""")
    # Esta parte da função serve somente para encontrar o primeiro valor para 
    # o algoritmo recursivo
    b = 1
    k_poss = [
            (int(sqrt(n)), int(sqrt(n))**2 - n),
            (int(sqrt(n)) + 1, int(sqrt(n) + 1)**2 - n)
            ]
    (a,k) = min(k_poss, key = lambda t: abs(t[1]))
    if k == 1:
        dictio = {'solution_x': a,
                'solution_y': b,
                'iterations' : 1}
        return dictio
    # Invocamos a função recursiva para simplificar os cálculos.
    else:
        return _chak_recu(a,b,n)
