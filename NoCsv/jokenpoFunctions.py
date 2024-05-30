#aqui temos uma função que receberá uma matriz e uma coluna, e retornará o maior num
def maisRepetidoDaColuna(mtz, col = int):
    indL = 0
    while indL < len(mtz[0]):
        if indL < 1:
            maior_num = mtz[0][0]
        elif mtz[col][indL] > maior_num:
            maior_num = mtz[col][indL]
        indL += 1
    return maior_num

#aqui temos uma função que entrega o lance vitórioso contra um lance previsto
#0 é pedra, 1 é papel, 2 é tesoura
def counterDoLance(lance = int):
    if lance == 0:
        return 1
    elif lance == 1:
        return 2
    return 0

#essa função calcula o resultado de um turno
#0 é pedra, 1 é papel, 2 é tesoura
def jokenpoResult(lance1 = int, lance2 = int):

    if lance1 == 0 and lance2 == 2:
        print('Você ganhou! Pedra ganha de tesoura')
        return 'victory'
    elif lance1 == 0 and lance2 == 1:
        print('Você perdeu! Pedra perde para papel')
        return 'defeat'
    elif lance1 == 1 and lance2 == 0:
        print('Você ganhou! Papel ganha da pedra')
        return 'victory'
    elif lance1 == 1 and lance2 == 2:
        print('Você perdeu! Papel perde para tesoura')
        return 'defeat'
    elif lance1 == 2 and lance2 == 1:
        print('Você ganhou! Tesoura ganha de papel')
        return 'victory'
    elif lance1 == 2 and lance2 == 1:
        print('Você perdeu! Tesoura perde para pedra')
        return 'defeat'
    print('empate')
    return 'draw'
    

            
