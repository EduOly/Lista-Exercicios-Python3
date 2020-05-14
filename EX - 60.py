from math import factorial
n =  int(input('Digite um número para calcular seu factorial: '))
c = n
fc = factorial(n)
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else ' = ', end='')
    c -=  1
print('{}'.format(fc))