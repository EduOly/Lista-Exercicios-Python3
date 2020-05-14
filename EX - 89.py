print('\33c')
student =  list( )
data = list()
grades = list()
view = 0 

print('\33[1m=\33[m'*30)
print(f"\33[1m{'[':<}{'CADRASTRO DE ALUNOS':^28}{']':>}\33[m")
print('\33[1m=\33[m'*30)

while True:
    print('-'*30)
    data.append(str(input('[Aluno(a)]: ')))
    n1 =  float(input('[Nota  1ª]: '))
    n2 = float(input('[Nota  2ª]: '))
    print('-'*30)
    grades.append(n1)
    grades.append(n2)
    data.append(grades[:])
    data.append((n1+n2)/2)
    student.append(data[:])
    grades.clear()
    data.clear()

    const =  str(input('Quer continuar? [S / N] ')).upper()[0]
    if const == 'N':
        break
print(' '*8)
print('\33[1m=\33[m'*30)
print(f"\33[1m{'[':<0}{'BOLETIM':^28}{']':>1}\33[m")
print('\33[1m=\33[m'*30)
print(f"{'No.NOME':<0}{' ':^18}{'MÉDIA':>1}")
print('-'*30)
for d in range(0, len(student)):
    print(f"{d}  \33[1m{student[d][0]:<24}\33[m",end='')
    print(f"\33[1;32m{student[d][2]:>.1f}\33[m")
print('-'*30)
print(' '*10)
    
while True:
    view = int(input('Mostra notos de qual aluno? (Digite 999 para sair ): '))
    if view == 999:
        break
    print('-'*35)
    print(f"{'|':<} Notas de {student[view][0]} são \33[1;32m{student[view][1]}\33[m {'|':>}")
    print('-'*35)
