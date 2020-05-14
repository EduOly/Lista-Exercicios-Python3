from datetime import date
print('{:=^38}'.format(' \33[1;31mCNN\33[m '))
#Entrada de dados
nas = int(input('Seu ano de nascimento: '))
#Manipulação da data atual do sistema
ano = date.today().year
ida = ano - nas
#Processor de Condiçoes aninhadas
#E saida de dados
if ida >= 9 and ida <= 13:
    print('Sua caategoria é: \33[1;32mMIRIN\33[m ')
if ida< 9:
    print('\33[1;31mNão está aptor a praticar o esporte!\33[m')
elif ida >= 14 and ida <= 18:
    print('Sua categoria é: \33[1;32mINFANTIL\33[m')
elif ida == 19:
    print('Sua categoria é: \33[1;32mJUNIOR\33[m ')
elif ida == 20:
    print('Sua categoria é: \33[1;32mSÊNIOR\33[m')
elif ida > 20:
    print('Sua categoria é: \33[1;32mMASTER\33[m')