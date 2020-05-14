'''
Faça um programa que tenha um função notas() que pode receber várias 
notas de alunos e vai retornar um dicionário com as seguintes informações:
 -- Quantidade de notas 
 -- A maior nota
 -- A menor nota 
 -- A média  de turma 
 -- A situação (opcional)
 Aducione também as doctring da função'''

print('\33c')

def notas(*n, s=False):
    """[Notas]
    Função para categorizar dados(Notas) a serem informadas 
    não inporta a quantidade de notas 
    Returns:
        [dci['total']] -- [Retorna o valor total de notas]
        [dci['maior']] -- [Retorna o valor maior das notas]
        [dci['menor']] -- [Retorna o valor menor das notas]
        [dci['média']] -- [Retorna o valor a médias das notas]
        [dci['situação']] -- [Retorna a situação do aluno]
    """
    dci = dict()
    dci['total'] = len(n)
    dci['maior'] = max(n)
    dci['menor'] = min(n)
    dci['média'] = (sum(n)/(dci['total']))

    if s == True:
        if dci['média'] >= 7:
            dci['situação'] = 'BOA'
        elif dci['média'] >= 5:
            dci['situação'] = 'RAZOÁVEL'
        else:
            dci['situação'] = 'RUIM'
    return dci

#Programa princinpal
print('-'*55)
print(notas(5.5, 9.5, 10, 6.5, s=True)) 
#help(notas)