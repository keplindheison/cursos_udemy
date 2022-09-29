perguntas = {
    'Pergunta 1':{
        'Pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5'
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2':{
        'Pergunta': 'Quanto é 3*2? ',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6'
        },
        'resposta_certa': 'c',
    },
}

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f"{pk}:{pv['Pergunta']}")

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f"[{rk}]:{rv}")

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('EHHHHHHH!!!! Você acertou!!!!')
        respostas_certas += 1
    else:
        print('Você errou!!!!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f' Sua porcentagem de acrto foi de {porcentagem_acerto}%')



