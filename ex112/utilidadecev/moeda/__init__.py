def moeda(x):
    return f'R${x:.0f},00'

def aumentar(x, a, f=False):
    m = x + ((a * x)/100)  
    if f == True:
        return moeda(m)
    else:
        return m

def diminuir(x, d, f=False):
    n = x - ((d * x)/100)
    if f == True:
        return moeda(n)
    else:
        return n


def dobro(x, f=False):
    d = x*2
    if f == True:
        return moeda(d)
    else:
        return d


def metade(x, f=False):
    m =  x / 2
    if f == True:
        return moeda(m)
    else:
        return m

def resumo(x, p, g):
    print('\33c')
    print('-'*30)
    print(f"{'|'} {'RESUMO DO VALOR':^26} {'|'}")
    print('-'*30)
    print(f"""Preço analizado:   {moeda(x)}
Dobro do preço:    {dobro(x)}
Metade do preço:   {metade(x, True)}
{p}% de aumento:    {aumentar(x, p,True)}
{g}% de redução:    {diminuir(x, g, True)}""")
    print('-'*30)
    print()