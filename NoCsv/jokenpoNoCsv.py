from random import randint
import jokenpoFunctions as jf

#wins são as vitórias da MAQUINA. 0 significa derrota e 1 vitória
wins = []

#aqui guardamos em que jogo nós estamos, essa váriavel vai servir para criarmos novas listas em jokenpo
roundInd = 0

# O primeiro histórico de jogadas da MAQUINA
round0 = []

#jokenpo é o histórico inteiro das jogadas da MAQUINA em 1 rodada
jokenpo = [round0]

#guardaremos tudo isso em uma matriz
jokenpo_DataFrame = [jokenpo, wins]

#aqui nos guardamos em que turno estamos no jokenpo
turn = 0



print('Bem vindo ao Jokenpo')
lance = int(input('Digite 0 para pedra, 1 para papel, 2 para tesoura, 3 para encerrar o jogo '))


#aqui nos definimos lances aleatórios até termos uma base de dados boa
if len(jokenpo) < 10:
    lance_maquina = randint(0, 2)
    str(roundInd)
    jokenpo['round'+roundInd].append(lance_maquina)
    int(roundInd)
else:
#aqui nos analisamos os lances do turno respectivo dos jogos anteriores, e pegamos o com maior probabilidade de 
#vitória
    lance_mais_provavel = jf.maisRepetidoDaColuna(jokenpo[round+roundInd], turn)
    lance_maquina = lance_mais_provavel
#não precisava da linha 36, só fiz para melhorar a compreensão

#aqui nos processamos o resultado e colocamos a saída na variável 'res'
res = jf.jokenpoResult(lance, lance_maquina)

#aqui nós processamos o resultado para definir como o programa irá proceder
if res == 'victory':
    wins.append(0)
    roundInd += 1
elif res == 'defeat':
    wins.append(1)
    roundInd += 1
elif res == 'draw':
    turn += 1
    jokenpo[round+roundInd].append(lance_maquina)




