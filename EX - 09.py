from cor import box_txt
box_txt('TABUADA')
n = int(input('Informe um número: '))

print('1x{0}= {1}\n'
      '2x{2}= {3}\n'
      '3x{4}= {5}\n'
      '4x{6}= {7}\n'
      '5x{8}= {9}\n'
      '6x{10}= {11}\n'
      '7x{12}= {13}\n'
      '8x{14}= {15}\n'
      '9x{16}= {17}\n'
      '10x{18}={19}'.format(n, n*1, n, n*2, n, n*3, n, n*4, n, n*5, n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))
