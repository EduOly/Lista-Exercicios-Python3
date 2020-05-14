from math import  sin, cos, tan, radians
print(' '*20)
print('{:=^30}'.format('  ÂNGULO '))
an = float(input('Qual valor do ângulo: '))
print('O valor do seno é de: {:.2f}'.format(sin(radians(an))))
print('O valor do coseno é de: {:.2f}'.format(cos(radians(an))))
print('O valor da tangênte é de: {:.2f}'.format( tan(radians(an))))
print('='*30)
