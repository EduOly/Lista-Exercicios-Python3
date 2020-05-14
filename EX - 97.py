'''Faça um programa que tenha a função chamada escreva().
que receba um texto qualquer como parãmetro e mostre uma
mensagem com  tamanho adaptátivo.'''
print('\33c')
def escreva(sms):
    print('~'*(len(sms)+4))
    print(f"  {sms}")
    print('~'*(len(sms)+4))

#Programa principal

escreva('CURSO EM VIDEO')
escreva('EDUARDO PROGRAMADOR')
escreva('OLÁ MUNDO')
escreva('Eduardo Soares de Oliveira')