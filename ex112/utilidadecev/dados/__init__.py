def leiaDinheiro(x):
    vali = False
    while not vali:
        entra = str(input(x)).replace(',','.').strip()
        if entra.isalpha() or entra == '':
            print(f'\33[1;31mERRO: \"{entra}\" é um preço inválido!\33[m')
        else:
            vali = True
            return float(entra)
        