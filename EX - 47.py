print('{:=^40}'.format(' NÚMEROS PARES '))
for c in range(1, 50, 2):
    c += 1
    print(f"\33[31m{c}\33[m", end=',' )
