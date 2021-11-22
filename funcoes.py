from random import randint


def jogarDado():
    dado = randint(1, 6)
    return dado


def resposta(msg):
    resp = str(input(msg))
    return resp
