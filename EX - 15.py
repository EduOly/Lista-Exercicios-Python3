print('{:=^30}'.format('  LOCALiZA '))
km = float(input('Informe a quandidade de kilometros: '))
di = int(input('Informe qauntos dias: '))
print('O preço total a pagar é de: R${:.2f}'.format((km*0.15)+(di*60)))