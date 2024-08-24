sexo = input('Qual o seu genero ?\n Sexo:')

if sexo == 'masculino':

    x = int(input('digite o seu peso em kg: '))
    y = int(input('digite a sua altura em cm: '))
    z = int(input('digite a sua idade: '))

    R = ((10 * x) + (6.25 * y) - (5 * z) + 5)

    print('Você gasta no minimo aproximadamente {} calorias por dia (não fazendo absolutamente nada)'.format(R))

    na = input('\n/////////////////////////////////////\n\nAgora qual o seu nivel de atividade fisica ?\n\n Pouco ativo (2-3 dias por semana)(digite: pouco)\n Levemente ativo (1 a 3 vezes por semana sem muito esforço)(digite: leve)\n Moderadamente ativo (3 a 5 vezes por semana)(digite: moderado)\n Muito ativo (6 a 7 dias por semana)(digite: muito)\n Extremamente ativo (2x por dia)(digite: extremo)\n\n NIVEL DE ATIVIDADE FISICA: ')

    if na == 'pouco':
        print('Seu gasto calorico não realizando nenhuma atividade fisica é de {} calorias'.format(R * 1.2))

    if na == 'leve':
        print('Seu gasto calorico realizando atividades fisicas levemente (1 a 3 vezes por semana sem muito esforço) é de {} calorias'.format(R * 1.375))

    if na == 'moderado':
        print('Seu gasto calorico realizando atividades fisicas moderadamente (3 a 5 vezes por semana)  é de {} calorias'.format(R * 1.55))

    if na == 'muito':
        print(
            'Seu gasto calorico realizando muitas atividades fisicas (6 a 7 dias por semana) é de {} calorias '.format(R * 1.725))

    if na == 'extremo':
        print('Seu gasto calorico realizando extremamente atividades fisicas (2x por dia) é de {} calorias'.format(R * 1.9))

if sexo == 'feminino':

    x = int(input('digite o seu peso em kg: '))
    y = int(input('digite a sua altura em cm: '))
    z = int(input('digite a sua idade: '))

    R1 = ((10 * x) + (6.25 * y) - (5 * z) - 161)

    print('Você gasta no minimo aproximadamente {} calorias por dia (não fazendo absolutamente nada)'.format(R1))

    na1 = input(
        '\n/////////////////////////////////////\n\nAgora qual o seu nivel de atividade fisica ?\n\n Pouco ativo (2-3 dias por semana)(digite: pouco)\n Levemente ativo (1 a 3 vezes por semana sem muito esforço)(digite: leve)\n Moderadamente ativo (3 a 5 vezes por semana)(digite: moderado)\n Muito ativo (6 a 7 dias por semana)(digite: muito)\n Extremamente ativo (2x por dia)(digite: extremo)\n\n NIVEL DE ATIVIDADE FISICA: ')

    if na1 == 'pouco':
        print('Seu gasto calorico não realizando nenhuma atividade fisica é de {} calorias'.format(R1 * 1.2))

    if na1 == 'leve':
        print('Seu gasto calorico realizando atividades fisicas levemente (1 a 3 vezes por semana sem muito esforço) é de {} calorias'.format(R1 * 1.375))

    if na1 == 'moderado':
        print('Seu gasto calorico realizando atividades fisicas moderadamente (3 a 5 vezes por semana)  é de {} calorias'.format(R1 * 1.55))

    if na1 == 'muito':
        print('Seu gasto calorico realizando muitas atividades fisicas (6 a 7 dias por semana) é de {} calorias '.format(R1 * 1.725))

    if na1 == 'extremo':
        print('Seu gasto calorico realizando extremamente atividades fisicas (2x por dia) é de {} calorias'.format(R1 * 1.9))