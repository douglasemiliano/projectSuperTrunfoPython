import random


def obterCartas (baralho, mao):
    while (len(mao)<6 and len(baralho) > 0):
        random.shuffle(baralho)
        mao.append(baralho[0])
        baralho.pop(0)
    return mao


def desenharCartas (mao):
    return print("\n"+
    "╔══════════════╗╔══════════════╗╔══════════════╗╔══════════════╗╔══════════════╗╔══════════════╗\n"+
    "║  ",mao[0][0],"  ║║  ",mao[1][0],"  ║║  ",mao[2][0],"  ║║  ",mao[3][0],"  ║║  ",mao[4][0],"  ║║  ",mao[5][0],"  ║\n"+
    "╠══════════════╣╠══════════════╣╠══════════════╣╠══════════════╣╠══════════════╣╠══════════════╣\n"+
    "║ FORÇA: ",mao[0][1]," ║║ FORÇA: ",mao[1][1]," ║║ FORÇA: ",mao[2][1]," ║║ FORÇA: ",mao[3][1]," ║║ FORÇA: ",mao[4][1]," ║║ FORÇA: ",mao[5][1]," ║\n"+
    "╠══════════════╣╠══════════════╣╠══════════════╣╠══════════════╣╠══════════════╣╠══════════════╣\n"+
    "║ MAGIA: ",mao[0][2]," ║║ MAGIA: ",mao[1][2]," ║║ MAGIA: ",mao[2][2]," ║║ MAGIA: ",mao[3][2]," ║║ MAGIA: ",mao[4][2]," ║║ MAGIA: ",mao[5][2]," ║\n"+
    "╚══════════════╝╚══════════════╝╚══════════════╝╚══════════════╝╚══════════════╝╚══════════════╝")
def desenharCartaIndividual (mao, escolha, mao2, escolha2):
    return print("\n"+
    "╔══════════════╗     ╔══════════════╗\n"+
    "║  ",mao[escolha-1][0],"  ║     ║  ",mao2[(escolha2)-1][0],"  ║\n"+
    "╠══════════════╣     ╠══════════════╣\n"+
    "║ FORÇA: ",mao[escolha-1][1]," ║     ║ FORÇA: ",mao2[(escolha2)-1][1]," ║\n"+
    "╠══════════════╣     ╠══════════════╣\n"+
    "║ MAGIA: ",mao[escolha-1][2]," ║     ║ MAGIA: ",mao2[(escolha2)-1][2]," ║\n"+
    "╚══════════════╝     ╚══════════════╝")

def desenharCartasBaixo (mao):
    return print("\n"+
    "       1               2               3               4               5               6        \n"+             
    "╔══════════════╗╔══════════════╗╔══════════════╗╔══════════════╗╔══════════════╗╔══════════════╗\n"+
    "║ SUPER TRUNFO ║║ SUPER TRUNFO ║║ SUPER TRUNFO ║║ SUPER TRUNFO ║║ SUPER TRUNFO ║║ SUPER TRUNFO ║\n"+
    "╠══════════════╣╠══════════════╣╠══════════════╣╠══════════════╣╠══════════════╣╠══════════════╣\n"+
    "║ SUPER TRUNFO ║║ SUPER TRUNFO ║║ SUPER TRUNFO ║║ SUPER TRUNFO ║║ SUPER TRUNFO ║║ SUPER TRUNFO ║\n"+
    "╠══════════════╣╠══════════════╣╠══════════════╣╠══════════════╣╠══════════════╣╠══════════════╣\n"+
    "║ SUPER TRUNFO ║║ SUPER TRUNFO ║║ SUPER TRUNFO ║║ SUPER TRUNFO ║║ SUPER TRUNFO ║║ SUPER TRUNFO ║\n"+
    "╚══════════════╝╚══════════════╝╚══════════════╝╚══════════════╝╚══════════════╝╚══════════════╝")    

def comparar(atributo, mao, escolha, escolha2, mao2, jogador1, jogador2, baralho, baralho2):
    if (atributo == 1):
        if(mao[escolha-1][1] > mao2[(escolha2)-1][1]):
            mao.pop(escolha-1)
            mao2.pop((escolha2)-1)
            mao = obterCartas(baralho, mao)
            mao2 = obterCartas(baralho2, mao2)            
            return 0

        elif(mao[escolha-1][1] == mao2[(escolha2)-1][1]):
            mao.pop(escolha-1)
            mao2.pop((escolha2)-1)
            mao = obterCartas(baralho, mao)
            mao2 = obterCartas(baralho2, mao2)
            return 2
            
        elif(mao[escolha-1][1] < mao2[(escolha2)-1][1]):
            mao.pop(escolha-1)
            mao2.pop((escolha2)-1)
            mao = obterCartas(baralho, mao)
            mao2 = obterCartas(baralho2, mao2)
            return 1

    elif (atributo == 2):
        if(mao[escolha-1][2] > mao2[(escolha2)-1][2]):
            mao.pop(escolha-1)
            mao2.pop((escolha2)-1)
            mao = obterCartas(baralho, mao)
            mao2 = obterCartas(baralho2, mao2)
            return 0

        elif(mao[escolha-1][2] == mao2[(escolha2)-1][2]):
            mao.pop(escolha-1)
            mao2.pop((escolha2)-1)
            mao = obterCartas(baralho, mao)
            mao2 = obterCartas(baralho2, mao2)
            return 2
        
        elif(mao[escolha-1][2] < mao2[(escolha2)-1][2]):
            mao.pop(escolha-1)
            mao2.pop((escolha2)-1)
            mao = obterCartas(baralho, mao)
            mao2 = obterCartas(baralho2, mao2)
            return 1

baralho = [["Bicho 01", 500, 100],
           ["Bicho 02",9.0, 400],
           ["Bicho 03",300,250],
           ["Bicho 04",300, 5.0],
           ["Bicho 05", 150, 300],
           ["Bicho 06", 250, 100],
           ["Bicho 07",200,500],
           ["Bicho 08",500,3.0],
           ["Bicho 09", 180, 150],
           ["Bicho 10",800, 0.0],
           ["Bicho 11", 0.0, 200],
           ["Bicho 12", 200, 2.0],
           ["Bicho 13", 400, 7.0],
           ["Bicho 14", 300, 5.0],
           ["Bicho 15",300,300],
           ["Bicho 16", 1.0,500],
           ["Bicho 17",5.0,600],
           ["Bicho 18", 300, 200],
           ["Bicho 19", 250, 200],
           ["Bicho 20", 400, 400]]


baralho2 = [["Bicho 01", 500, 100],
           ["Bicho 02",9.0, 400],
           ["Bicho 03",300,250],
           ["Bicho 04",300, 5.0],
           ["Bicho 05", 150, 300],
           ["Bicho 06", 250, 100],
           ["Bicho 07",200,500],
           ["Bicho 08",500,3.0],
           ["Bicho 09", 180, 150],
           ["Bicho 10",800, 0.0],
           ["Bicho 11", 0.0, 200],
           ["Bicho 12", 200, 2.0],
           ["Bicho 13", 400, 7.0],
           ["Bicho 14", 300, 5.0],
           ["Bicho 15",300,300],
           ["Bicho 16", 1.0,500],
           ["Bicho 17",5.0,600],
           ["Bicho 18", 300, 200],
           ["Bicho 19", 250, 200],
           ["Bicho 20", 400, 400]]
print("    ╔═══════════════════════════════════════════════════════════════════════════════════╗")
print("    ║    ____   _____  __  __  __     __ ___  _   _  ____    ___       _      ___       ║")
print("    ║   | __ ) | ____||  \/  | \ \   / /|_ _|| \ | ||  _ \  / _ \     / \    / _ \      ║")
print("    ║   |  _ \ |  _|  | |\/| |  \ \ / /  | | |  \| || | | || | | |   / _ \  | | | |     ║")
print("    ║   | |_) || |___ | |  | |   \ V /   | | | |\  || |_| || |_| |  / ___ \ | |_| |     ║")
print("    ║   |____/ |_____||_|  |_|    \_/   |___||_| \_||____/  \___/  /_/   \_\ \___/      ║")
print("    ║                                                                                   ║")
print("    ║    ____   _   _  ____   _____  ____    _____  ____   _   _  _   _  _____   ___    ║")
print("    ║   / ___| | | | ||  _ \ | ____||  _ \  |_   _||  _ \ | | | || \ | ||  ___| / _ \   ║")
print("    ║   \___ \ | | | || |_) ||  _|  | |_) |   | |  | |_) || | | ||  \| || |_   | | | |  ║")
print("    ║    ___) || |_| ||  __/ | |___ |  _ <    | |  |  _ < | |_| || |\  ||  _|  | |_| |  ║")
print("    ║   |____/  \___/ |_|    |_____||_| \_\   |_|  |_| \_\ \___/ |_| \_||_|     \___/   ║")
print("    ║                                                                                   ║")
print("    ╚═══════════════════════════════════════════════════════════════════════════════════╝")


menu = 0
while (menu != 3):
    print("                            ╔═══════════════════════════════════╗")
    print("                            ║  __  __   _____   _   _   _   _   ║")
    print("                            ║ |  \/  | | ____| | \ | | | | | |  ║")
    print("                            ║ | |\/| | |  _|   |  \| | | | | |  ║")
    print("                            ║ | |  | | | |___  | |\  | | |_| |  ║")
    print("                            ║ |_|  |_| |_____| |_| \_|  \___/   ║")
    print("                            ║                                   ║")
    print("                            ╠═══════════════════════════════════╣")
    print("                       ╔════╩═════════╗╔══════════════╗╔════════╩════╗\n"+
          "                       ║ 1 = INICIAR  ║║  2 = REGRAS  ║║   3 = SAIR  ║\n"+
          "                       ╚══════════════╝╚══════════════╝╚═════════════╝")
    menu = int(input("O que deseja fazer? "))
    if (menu == 1):
        placar1 = 0.0
        placar2 = 0.0
        final = False
        jogador1 = str.upper(input("Qual o nome do jogador 01? "))
        jogador2 = str.upper(input("Qual o nome do jogador 02? "))
        mao = []
        mao2 = []
        while (final == False):
                print("                   ╔═════════════════════════════════════════════════════╗")
                print("                   ║  ____    _          _       ____      _      ____   ║")
                print("                   ║ |  _ \  | |        / \     / ___|    / \    |  _ \  ║")
                print("                   ║ | |_) | | |       / _ \   | |       / _ \   | |_) | ║")
                print("                   ║ |  __/  | |___   / ___ \  | |___   / ___ \  |  _ <  ║")
                print("                   ║ |_|     |_____| /_/   \_\  \____| /_/   \_\ |_| \_\ ║")
                print("                   ║                                                     ║")
                print("                   ╚══════════════╦══════════════════════╦═══════════════╝")
                print("                        ╔═════════╩═════════╗  ╔═════════╩═════════╗")
                print("                        ║       ",placar1,"       ║  ║       ",placar2,"       ║")
                print("                        ╚═══════════════════╝  ╚═══════════════════╝")

                                                    
            
                print("\n             ╔═════════════════════════════════════════════════════════════════╗")
                print("             ║      _    ___     ____      _      ____     ___    ____      _  ║")
                print("             ║     | |  / _ \   / ___|    / \    |  _ \   / _ \  |  _ \    / | ║")
                print("             ║  _  | | | | | | | |  _    / _ \   | | | | | | | | | |_) |   | | ║")
                print("             ║ | |_| | | |_| | | |_| |  / ___ \  | |_| | | |_| | |  _ <    | | ║")
                print("             ║  \___/   \___/   \____| /_/   \_\ |____/   \___/  |_| \_\   |_| ║")
                print("             ║                                                                 ║")
                print("             ╚═════════════════════════════════════════════════════════════════╝")
                                                                        

                mao = obterCartas(baralho, mao)
                mao2 = obterCartas(baralho2, mao2)
                desenharCartasBaixo(mao)

                escolha = int(input("Escolha uma carta: "))

                ####### JOGADOR 2 ######

                print("\n             ╔═══════════════════════════════════════════════════════════════════╗")
                print("             ║      _    ___     ____      _      ____     ___    ____    ____   ║")
                print("             ║     | |  / _ \   / ___|    / \    |  _ \   / _ \  |  _ \  |___ \  ║")
                print("             ║  _  | | | | | | | |  _    / _ \   | | | | | | | | | |_) |   __) | ║")
                print("             ║ | |_| | | |_| | | |_| |  / ___ \  | |_| | | |_| | |  _ <   / __/  ║")
                print("             ║  \___/   \___/   \____| /_/   \_\ |____/   \___/  |_| \_\ |_____| ║")
                print("             ║                                                                   ║")
                print("             ╚═══════════════════════════════════════════════════════════════════╝")
                      
                mao2 = obterCartas(baralho2, mao2)
                desenharCartasBaixo(mao2)
                escolha2 = int(input("Escolha uma carta: \n"))
                ##atributo = str.upper("Qual atributo você quer comparar?")
                atributo = int(input("Qual atributo deseja comparar? \n 1 para FORÇA e 2 para MAGIA:\n" ))

                win = comparar(atributo, mao, escolha, escolha2, mao2, jogador1, jogador2, baralho, baralho2)
                if(win == 0):
                    print(jogador1,"GANHOU 1 PONTO!")
                    placar1 += 1
                elif(win == 1):
                    print(jogador2,"GANHOU 1 PONTO!")
                    placar2 += 1
                elif(win == 2):
                    print("EMPATE, OS DOIS JOGADORES PONTUARAM!")
                    placar2 += 1
                    placar1 += 1
                    
                if (placar1 >= 2 or placar2 >=2):
                    final = True
                          

                desenharCartaIndividual(mao, escolha, mao2, escolha2)
                #desenharCartaIndividual(mao2, escolha2)
        print("FIM DO JOGO")
        if(placar1 > placar2):
            print("O jogador ",jogador1, "Ganhou o jogo com o placar de",placar1,"pontos")
        elif(placar1<placar2):
            print("O jogador ",jogador2, "Ganhou o jogo com o placar de",placar2,"pontos")


    elif (menu == 2):
        print("                 ╔════════════════════════════════════════════════════════╗")
        print("                 ║     ____    _____    ____   ____       _      ____     ║")
        print("                 ║    |  _ \  | ____|  / ___| |  _ \     / \    / ___|    ║")
        print("                 ║    | |_) | |  _|   | |  _  | |_) |   / _ \   \___ \    ║")
        print("                 ║    |  _ <  | |___  | |_| | |  _ <   / ___ \   ___) |   ║")
        print("                 ║    |_| \_\ |_____|  \____| |_| \_\ /_/   \_\ |____/    ║")
        print("                 ║                                                        ║")
        print("                 ╠════════════════════════════════════════════════════════╣")                                                                                                    
        print("           ╔═════╩════════════════════════════════════════════════════════╩════╗")
        print("           ║                                                                   ║")
        print("           ║   Lorem ipsum dolor sit amet, consectetur adipiscing elit.        ║")
        print("           ║   Phasellus euismod velit euismod facilisis bibendum. Fusce       ║")
        print("           ║   tempus tellus in ornare mattis. Aliquam in magna vitae eros     ║")
        print("           ║   finibus sodales. Quisque metus diam, faucibus at laoreet at,    ║")
        print("           ║   convallis in risus. Morbi suscipit lacus ut mauris dignissim    ║") 
        print("           ║   blandit. Integer ac ex in leo venenatis elementum. Praesent     ║")
        print("           ║   eget lectus interdum velit imperdiet ultricies non nec dui.     ║")
        print("           ║   Curabitur bibendum dui at commodo maximus. Nunc non ipsum sed   ║")
        print("           ║   elit sollicitudin viverra. In vel ultrices dui. Fusce mattis    ║")
        print("           ║   condimentum metus rutrum rhoncus. Cras interdum risus elementum ║")
        print("           ║   nunc ornare lobortis. Fusce semper tortor in libero maximus,    ║")
        print("           ║   quis sodales elit pulvinar. Integer augue diam, sodales sed     ║")
        print("           ║   purus nec, mollis scelerisque ipsum. Sed ultrices quis sem at   ║")
        print("           ║   eleifend.                                                       ║")
        print("           ║                                                                   ║")
        print("           ║   Praesent efficitur sagittis lacus at malesuada. Suspendisse     ║")
        print("           ║   potenti. Mauris venenatis venenatis tristique. Sed vehicula     ║")
        print("           ║   velit magna, et sagittis lacus rutrum eu. Suspendisse purus     ║")
        print("           ║   lacus, vestibulum ut urna in, interdum feugiat purus. Aenean    ║")
        print("           ║   scelerisque quis sapien at pharetra. Nulla pretium eros         ║")
        print("           ║   aliquam commodo dignissim. Aenean quis est mollis, tincidunt    ║")
        print("           ║   ipsum vel, rhoncus ante. Proin bibendum libero ligula, ut       ║")
        print("           ║   ullamcorper neque imperdiet vel. Phasellus vel metus dapibus,   ║")
        print("           ║   tincidunt magna eu, sollicitudin elit. Nunc at ante ullamcorper ║")
        print("           ║   neque pharetra sagittis nec ac purus. Morbi at lacus libero.    ║")
        print("           ║   In sed orci tempor, pharetra nunc vel, vulputate urna.          ║")
        print("           ║                                                                   ║")
        print("           ╚═══════════════════════════════════════════════════════════════════╝")




