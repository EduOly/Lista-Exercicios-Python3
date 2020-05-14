def leiaDinheiro(x):
    while True:
        ok = False
        v = input(x)
        if v.isnumeric() or v[:(v.find(','))].isnumeric() or v.find('.') :
            if v.find('.'):
                vali = float(v.replace('.', '.'))
                ok = True
            vali = float(v.replace(',','.'))
            ok = True
                
        else:
            print('\33[1;31m[ERRO] Valor não númerico!\33[m')
        if ok == True:
            break
    return vali
            