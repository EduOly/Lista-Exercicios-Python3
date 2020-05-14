'''
Crie  um prongrama que  faça uma seguência de fibonacci 
'''
print('-'*30)
print(' Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos ?: '))
t1 = 0
t2 = 1
c = 0 
print('-'*30)
print('(', end='')
while c  <= n:
    t3 = t1 + t2
    print('{}'.format(t3),end=', ')
    t1 = t2
    t2 = t3
    c += 1
print('..)')