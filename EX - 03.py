from cor import box_txt
box_txt('Calculadora soma binária')
n1 = int(input('Informe um primeiro número para soma: '))
n2 = int(input('Informe um segundo número para a soma: '))
sm = n1+n2
print("A soma entre os números informados é de: \033[32m{}\033[m".format(sm))