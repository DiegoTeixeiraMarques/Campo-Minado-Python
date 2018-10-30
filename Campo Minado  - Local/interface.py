import controle
import subprocess


if __name__ == '__main__':
    
    tamCampo = int(input("Informe o tamanho do campo (ex.: 5): "))
    nBombas = int(input("Informe a quantidade de Bombas no campo (ex.: 10): "))
    
    subprocess.call('cls', shell=True)
    cm = controle.Campo(tamCampo, tamCampo, nBombas)
    cm.gerarBombas(cm.campoMinado, cm.nBombas, cm.nLinha, cm.nBombas)
    totalJogadas = cm.nJogadas

    while (cm.areaLivre > cm.nBombas):

        print('Atenção!\n', 'As linhas e Colunas variam de', 0, 'à', (len(cm.campoLimpo)-1))

        cm.mostrarCampo(cm.campoLimpo)
        print('--> Você tem', cm.nJogadas,'/', totalJogadas, 'jogadas restantes')
        print('--> Ainda existem', cm.areaLivre, 'áreas para decobrir.', '\n')
        linha = int(input("Informe a linha: "))
        coluna = int(input("Informe a coluna: "))
        subprocess.call('cls', shell=True)
        cm.campoLimpo, codRetorno = cm.jogada(cm.campoLimpo, cm.campoMinado, cm.nJogadas, linha, coluna)
        if (codRetorno == 0):
            continue
        elif (codRetorno == 1):
            cm.areaLivre = cm.contaAreaslivres(cm.campoLimpo)
            cm.nJogadas = cm.nJogadas - 1
        else:
            cm.mostrarCampo(cm.campoMinado)
            cm.areaLivre = 0
        #cm.mostrarCampo(cm.campoMinado)

    if(cm.areaLivre == nBombas):
        subprocess.call('color b', shell=True)
        cm.mostrarCampo(cm.campoLimpo)
        print('Parabéns, você ganhou!')
            
            

    