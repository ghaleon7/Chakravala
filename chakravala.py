# -*- coding: utf-8 -*-
"""
Este código Python serve para treinar e implementar recursão no código
A ideia será resolver a equação de Pell x^2 - ny^2 = 1 usando Chakravala, 
o método indiano
"""
import math
import numpy as np

from ._utils import m_method, compose

def chakravala(n):
    """
    Este método resolve a equação x^2 - ny^2 = 1 com soluções inteiras.
    O número n deve ser inteiro, positivo e não-quadrado.
    Devolve um dicionário com as soluções de x, y e quantas iterações 
    foram necessárias
    Argumentos:
        n - int
    Exemplo:
        x^2 - 3y^2 = 1
        Solução: x = 7, y = 4
        Deve devolver: {'solution_x': 2, 'solution_y': 1, 'iterations': 1}
    """
    #Estas são as excepções para as quais temos de estar preparados
    if n < 0:
        raise ValueError("O número deve ser positivo")
    if not isinstance(n, int):
        raise ValueError("O parâmetro deve ser inteiro")
    if math.sqrt(n).is_integer():
        raise ValueError("Não pode ser um quadrado perfeito")
     #Isto inicializa a primeira solução: a^2 - nb^2 = k
    b = 1
    hips = (int(math.sqrt(n)), 1 + int(math.sqrt(n)))
    values = (abs(hips[0]**2 - n), abs(hips[1]**2 - n))
    a = hips[np.argmin(values)]
    k = a**2 - n
    #Este array contém a primeira solução desta equação
    results = (a,b,k)
    i = 1
    while abs(results[2]) not in set((1,2)):
        a_0, b_0, k_0 = a, b, k
        m = m_method(a_0, b_0, k_0, n)
        brahma_array = (m, 1, m**2 - n)
        w = compose(results, brahma_array, n)
        a = int(w[0]/abs(k_0))
        b = int(w[1]/abs(k_0))
        k = int(w[2]/k_0**2)
        results = (a,b,k)
        i += 1
    if results[2] == 1:
        dictio = {'solution_x': results[0],
                'solution_y': results[1],
                'iterations' : i}
        return dictio
    elif results[2] == -1:
        results = compose(results, results, n)
        dictio = {'solution_x': results[0],
                'solution_y': results[1],
                'iterations' : i}
        return dictio
    elif abs(results[2]) == 2:
        results = compose(results, results, n)
        results = [int(results[0]/2), int(results[1]/2), 1]
        dictio = {'solution_x': results[0],
                'solution_y': results[1],
                'iterations' : i}
        return dictio

def chakravala_terno(n):
    """
    Este método resolve a equação x^2 - ny^2 = 1 com soluções inteiras.
    O número n deve ser inteiro, positivo e não-quadrado.
    Devolve um terno com as soluções de x, y
    A última coordenada, k, confirma que obtemos 1 com estas soluções
    Argumentos:
        n - int
    Exemplo:
        x^2 - 3y^2 = 1
        Solução: x = 7, y = 4
        Deve devolver: (7,4,1)
    """
    a = chakravala(n)['solution_x']
    b = chakravala(n)['solution_y']
    k = a**2 - n*b**2
    results = (a,b,k)
    return results