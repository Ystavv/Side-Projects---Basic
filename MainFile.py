from interface import *
from time import sleep
from funcoes import *

cabecalho('SIMULADOR DE DADO')
print(f'{cores["Amarelo"]}{"Este programa simplesmente joga uma dado.":^60}{cores["Amarelo"]}')
linha()

while True:
    try:
        resp = resposta(f'Quer Jogar o dado? '
                        f'[{cores["Verde"]}Sim{cores["Default"]}/'
                        f'{cores["Vermelho"]}Não{cores["Default"]}]: ').strip().upper()[0]

        while resp not in 'SN':
            linha()
            print(f'{cores["Vermelho"]}Por favor, dígite somente SIM ou NÃO.{cores["Default"]}')
            linha()
            resp = resposta(f'Quer Jogar o dado? '
                            f'[{cores["Verde"]}Sim{cores["Default"]}/'
                            f'{cores["Vermelho"]}Não{cores["Default"]}]: ').strip().upper()[0]

    except (ValueError, TypeError, IndexError):
        linha()
        print(f'{cores["Vermelho"]}ERRO: Resposta inválida!{cores["Default"]}')
        linha()
    except KeyboardInterrupt:
        linha()
        print(f'{cores["Vermelho"]}O Usuário preferiu não digitar uma resposta!{cores["Default"]}')
        linha()
    else:
        if resp in 'S':

            print(f'{cores["Verde"]}jogando o dado ', end='')
            for c in range(0, 3):
                print(f'.', end='')
                sleep(0.5)
            print()
            sleep(1)
            print(f'O Dado caiu com o número {cores["Azul"]}{jogarDado()}{cores["Default"]}.')

        elif resp in 'N':
            linha()
            cabecalho('Obrigado por jogar, volte sempre!')
            cabecalho('FIM DE SIMULAÇÃO')
            break
