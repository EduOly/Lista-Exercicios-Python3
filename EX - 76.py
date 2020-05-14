print('\33c')
print(' '*10)
print('\33[1;34m-\33[m'*40)
print(f'\33[1;32m{"LISTA DE PREÇOS":^40}\33[m')
print('\33[1;34m-\33[m'*40)
tabela =  ('Lápis',1.75,'Borracha', 2.00,
 'Caderno', 15.00, 'Estojo', 25.00,'Transferidor', 4.50,
  'Compasso', 9.99, 'Mochila', 120.00, 'Caneta', 22.30, 'Livro', 34.90)

for c in range(0, len(tabela), 2):
    print(f'\33[1;33m{tabela[c]:.<30}\33[m\33[1;32mR$ {tabela[c+1]:>7.2f} \33[m')
print('\33[1;34m-\33[m'*40)
print((' '*10))
