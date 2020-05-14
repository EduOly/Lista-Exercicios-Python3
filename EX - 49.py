print('\33[1;31m[{:=^30}]\33[m'.format(' TABUADA MULT '))
print('-=-'*5)
num = int(input('Digite um número: '))
print('-=-'*5)
for ct in range (0, 10):
    t = ct*num
    print('\33[1;36m[ {} X {} ]\33[m= \33[1;32m{}\33[m'.format( ct, num, t ))
print('-=-'*5)