from emoji import emojize
from time import sleep
for c in range(-10, 1):
    print("\33[1;32m[ {:-^28} ]\33[m".format(c))
    sleep(1)
print('\33[1;31m[{:=^30}]\33[m'.format(' ESTOROUUUU!!! '))
print(emojize(':boom:'*18, use_aliases=True ))