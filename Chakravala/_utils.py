# -*- coding: utf-8 -*-
import numpy as np

# Cálculo do máximo divisor comum
def gcdxy(a, b):
    """
    Esta função calcula o máximo divisor comum entre a e b 
    de forma a resolver a equação ax + by = mdc(a,b).
    Visto em: https://www.geeksforgeeks.org/python-program-
    for-basic-and-extended-euclidean-algorithms-2/
    Argumentos:
        - a,b - int
    Devolve:
        - gcd, x, y - int
    Exemplo:
        gcdxy(15,8)
            >> (1, -1, 2)
    """
    if a == 0 :   
        return b,0,1         
    gcd,x_i,y_i = gcdxy(b%a, a)  
    x,y = y_i - (b//a) * x_i, x_i
    return gcd,x,y 

# Cálculo do inverso multiplicativo modular
def modinv(b,n):
    """
    Esta função calcula o inverso multiplicativo de b módulo n
    Argumentos:
        b, n - int
    Devolve
        x%n - int
    Exemplo:
        modinv(3,5)
            >> 2
    """
    if 0 <= n < 2:
        raise ValueError("Não podemos usar o módulo 1, ou 0")
    gcd, x, y = gcdxy(b,n)
    if gcd == 1:
        return x%n
    else:
        raise ValueError("Não existe inverso, o mdc é {}".format(gcd))
        
# =============================================================================
# OPERAÇÕES INTERNAS À CHAKRAVALA
# =============================================================================

def compose(lst0,lst1,n):
    """
    Este é um método auxiliar que toma dois ternos e usa a regra de composição
    necessária para usar o método da Chakravala.
    (a,b,k)*(c,d,k') = (ac - nbd, ad + bc, kk')
    Argumentos:
        a,b,k - int
    Devolve:
        composition - int
    Exemplo:
        compose([3,2,1],[3,2,1],2)
            >> (17,12,1)
    """
    composition = (
            lst0[0]*lst1[0] + lst0[1]*lst1[1]*n, 
            lst0[0]*lst1[1] + lst0[1]*lst1[0], 
            lst0[2]*lst1[2])
    return composition

def m_method(a,b,k,n):
    """
    Este é um método auxiliar que procura o melhor valor para um parâmetro do 
    método Chakravala
    Argumentos:
        a,b,k,n - int
    Devolve:
        vect[mins] - int
    Exemplo:
        m_method(2,1,2,2)
            >> 2
    """
    first_m = (-a*modinv(b,k)) % abs(k)
    while abs(first_m) < np.sqrt(n):
        first_m = first_m + abs(k)
    vect = [first_m, first_m - abs(k)]
    quadrated_m_possible = [abs(i**2 - n) for i in vect]
    mins = np.argmin(quadrated_m_possible)
    return vect[mins]
