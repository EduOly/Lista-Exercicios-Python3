b = 'BREACK'
print(f"{b:-^30}")
s = c = 0
while True:
    n =  int(input('Ditite um valor[999 para para]: '))
    if n == 999:
         break
    s += n 
    c += 1
print(f'foram digitados {c} números e a soma entre eles é {s}.')
