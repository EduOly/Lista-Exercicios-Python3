def moeda(x):
    return f'R${x:.0f},00'

def aumentar(x, a):
    m = x + ((a * x)/100)  
    return m

def diminuir(x, d):
    n = x - ((d * x)/100)
    return n


def dobro(x):
    d = x*2
    return d


def metade(x):
    m =  x / 2
    return m