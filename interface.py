cores = {'Vermelho': '\033[31m',
         'Verde': '\033[32m',
         'Amarelo': '\033[33m',
         'Azul': '\033[34m',
         'Default': '\033[m'}


def linha(simb='-', tam=60, cor=cores['Default']):
    print(f'{cor}{simb}{cor}' * tam)


def cabecalho(titulo, simb='-', tam=60, ColorLine=cores['Default'], TitleColor=cores['Amarelo']):
    print(f'{ColorLine}{simb}{ColorLine}' * tam)
    print(f'{TitleColor}{titulo:^60}{TitleColor}')
    print(f'{ColorLine}{simb}{ColorLine}' * tam)
