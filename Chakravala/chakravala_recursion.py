# -*- coding: utf-8 -*-
"""
Esta é uma nova implementação do algoritmo Chakravala para resolução de 
equações x^2 - Dy^2 = 1 com soluções inteiras. Esta implementação usa recursão.
"""

from math import sqrt
from _utils import m_method, compose

def _chak_recu(a,b,N,i=2):
    """
    Função recursiva que calcula os valores de x e y.
    Argumentos:
        a,b,N - int
    Devolve:
        dictio - dict
    """
    # Inicialização do primeiro valor
    k = a**2 - N*b**2
    # Composição de ternos
    m = m_method(a,b,k,N)
    results = (a,b,k)
    brahma = (m, 1, m**2 - N)
    w = compose(results, brahma, N)
    # Diminuição do valor absoluto das soluções
    a_ = int(w[0]/abs(k))
    b_ = int(w[1]/abs(k))
    k_ = int(w[2]/k**2)
    # Inicialização do vetor de dimensões atualizadas
    w = (a_,b_,k_)
    # Solução
    dictio = {'sol_x': a_,
              'sol_y': b_,
              'its': i}
    # Casos especiais que terminam a realização de contas demoradas.
    if k_ == 1:
        return dictio
    elif k_ == -1:
        w = compose(w, w, N)
        dictio = {'sol_x': w[0],
                'sol_y': w[1],
                'its' : i}
        return dictio
    elif k_ == 2:
        w = compose(w, w, N)
        w = [int(w[0]/2), int(w[1]/2), 1]
        dictio = {'sol_x': w[0],
                'sol_y': w[1],
                'its' : i}
        return dictio
    # Se não obtivermos nenhum dos valores anteriores, repetimos o cálculo
    else:
        ans = _chak_recu(a_,b_,N,i=i+1)
    return ans


def chakravala_rec(n):
    """
    Esta função resolve a equação de Pell x^2 - ny^2 = 1 em números inteiros.
    O input "n" deve ser positivo, inteiro e não-quadrado. 
    Esta versão usa recursão para efetuar os cálculos. 
    A solução vem dada em formato de dicionário. A chave "solution_x" diz 
    respeito ao valor de x que resolve a equação e a chave "solution_y" diz 
    respeito ao valor de y que resolve a equação. A chave "iterations" indica
    quantas iterações foram precisas.
    Exemplo:
        >> chakravala_rec(7)
        >> {'solution_x': 8, 'solution_y': 3, 'iterations': 2}
    Argumentos:
        n - inteiro
    Devolve:
        dictio - dict
    """
    # Estas são as exceções para as quais temos de estar preparados
    if n < 0:
        raise ValueError(f"""Foi usado o número {n}. Para este cálculo, O
                         número deve ser positivo""")
    if not isinstance(n, int):
        raise ValueError(f"""Foi usado o número {n}. Para este cálculo, 
                         o parâmetro deve ser inteiro""")
    if sqrt(n).is_integer():
        raise ValueError(f"""Foi usado o número {n}. Para este cálculo, o 
                         parâmetro não pode ser um quadrado perfeito""")
    # Esta parte da função serve somente para encontrar o primeiro valor para 
    # o algoritmo recursivo
    b = 1
    sq_int = int(sqrt(n))
    k_poss = [
            (sq_int, sq_int**2 - n),
            (sq_int + 1, (sq_int + 1)**2 - n)
            ]
    # Este passo seleciona o tuplo com o menor valor absoluto na segunda coordenada
    (a,k) = min(k_poss, key = lambda t: abs(t[1]))
    # Pode dar-se o caso de se obter o valor ótimo apenas com o primeiro 
    # parâmetro. Geralmente acontece a números que estão muito perto de um 
    # número quadrado.
    if k == 1:
        dictio = {'sol_x': a,
                'sol_y': b,
                'its' : 1}
        return dictio
    # Invocamos a função recursiva para simplificar os cálculos.
    else:
        return _chak_recu(a,b,n)
