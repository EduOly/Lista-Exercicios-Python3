def moeda(x=0):
    return f'R${x:.0f},00'

def aumentar(x=0, a=0):
    m = x + ((a * x)/100)  
    return m

def diminuir(x=0, d=0):
    n = x - ((d * x)/100)
    return n


def dobro(x=0):
    d = x*2
    return d


def metade(x=0):
    m =  x / 2
    return m