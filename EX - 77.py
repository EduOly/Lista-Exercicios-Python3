'''
Crie um progrma que tenha uma tupla 
com vária palavras (não usar acentos).
Depois disso, você deve mostrar, para 
cada palavra, quais são as suas vogais
'''
print(' '*10)
pala = ('Aprender', 'Programar', 'linguagem', 
'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar',
 'Trabalhar', 'Mercado', 'Programador', 'Futuro')
for p in pala:
    print(f'\nAs palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
print(' '*10)