import controle


if __name__ == '__main__':
    
    tamCampo = int(input("Informe o tamanho do campo (ex.: 5): "))
    nBombas = int(input("Informe a quantidade de Bombas no campo (ex.: 10): "))
    
    cm = controle.Campo(tamCampo, tamCampo, nBombas)
    #linha = int(input("Informe a linha: "))
    #coluna = int(input("Informe a coluna: "))
    #cm.jogada(linha, coluna, cm, cm.nJogadas)
    #print(cm)
    #cm.showgrid(cm)   #parametro passado é o endereco de memoria [erro]
    #print('Você tem', cm.nJogadas, 'jogadas restantes')
    