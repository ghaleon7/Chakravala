# -*- coding: utf-8 -*-
import math

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
        m - int
    Exemplo:
        m_method(2,1,2,2)
            >> 2
    """
    #   Calcula o primeiro valor de m
    m_1 = (-a*modinv(b,k)) % abs(k)  
    
    #   Queremos que o valor de |m^2 - n| seja mínimo
    while abs(m_1) < math.sqrt(n):
        m_1 = m_1 + abs(k)
    
    #   Com as somas anteriores, podemos ter passado um valor menor
    m_0 = m_1 - abs(k)
    
    #   Comparamos os outputs
    appr_1 = abs(m_1**2-n)
    appr_0 = abs(m_0**2-n)
    
    #   Procuramos, dos dois valores a testar, qual nos dá um valor mínimo
    if appr_1 - appr_0 > 0:
        return m_0
    else:
        return m_1
