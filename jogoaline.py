import random
import os
from time import sleep
import pygame

pygame.init()
Saude=10
VidaSocial=10
Dinheiro=10
Fama=10
Nota=10

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def cronometro(tempo):
    while tempo:
        min, seg = divmod(tempo, 30)
        timer = '{:02d}:{:02d}'.format(min, seg)
        print(timer, end='\r')
        sleep(1)
        tempo -= 1
        
def imprime_lentamente(texto):
    for caractere in texto:
        print(caractere, end="", flush=True)
        sleep(0.1)
    
    
def game_over():
    limpar()
    pygame.init()
    
    print("\n\n")
    print("         _____                          ____ ")               
    print("        / ____|                        / __ \  ")                
    print("        | |  __  __ _ _ __ ___   ___   | |  |  _   __ _  _ __ ")
    print("        | | |_ |/ _` | '_ ` _ \ / _ \  | |  | \ \ / /  _ \ '__|")
    print("        | |__| | (_| | | | | | |  __/  | |__|  \ V /   __/ |   ")
    print("         \_____|\__,_|_| |_| |_|\___|  \____/   \_/  \___|_|   ")
    print('Criador:')
    imprime_lentamente("  -GAME OVER\n")
    exit()

def verificar_game_over(Saude, VidaSocial, Dinheiro, Fama, Nota):
    nao_tem_saude = Saude <= 0
    nao_tem_VidaSocial = VidaSocial <= 0
    nao_tem_Dinheiro = Dinheiro <= 0
    nao_tem_Fama = Fama <= 0
    nao_tem_Nota = Nota <= 0
    perdeu = nao_tem_Dinheiro or nao_tem_Fama or nao_tem_Nota or nao_tem_saude or nao_tem_VidaSocial
    
    if perdeu:
        game_over()

limpar()
print("\nCriador:")
imprime_lentamente("  -Olá gamer (＾∇＾). Eu sou a criadora desse Jogo.\n  -Para começar sua aventura como progamador, informe seu nome: ")
Nome=str(input())
limpar()
print("\nCriador:")
imprime_lentamente("  -Com a minha onipotência irei invocar um menu:\n")
sleep(2)
limpar()
imprime_lentamente("  -Quase lá...")
sleep(5)
limpar()
imprime_lentamente("  -Prontiinho:\n")

def JogoFacil(Nome2,Saude,VidaSocial,Dinheiro,Fama,Nota):
    
    limpar()
    pygame.init()
   
    print("\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-JOGO COMEÇOU-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n")
    print("\nNarrador:")
    imprime_lentamente("  -"+Nome2+" você está no ultimo período da faculdade de Ciência da Computação, você vai passar por varías situações ao decorrer do jogo\n  -Boa Sorte\n\n  -Agora vamos começar:\n")
    
    cronometro(3)
    limpar()
    
    print("\nNarrador:")
    imprime_lentamente("  -Você encontrou com seu professor (Rafael) no corredor\n")
    print("\nRafael:")
    imprime_lentamente("  -Olá "+Nome2+" eu abri uma vaga em um projeto extensão, você quer participar?")
    
    Faculdade1 = str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade1 == "S":
        limpar()
        print("\n"+Nome2+":")
        imprime_lentamente("  -Sim professor eu aceito, obrigado.\n")
        print("\nRafael:")
        imprime_lentamente("  -A propósito valeu  nota !\n")
        print("\nNarrador:")
        imprime_lentamente("  -Okay sua jornada de trabalho começa aqui ヽ(^。^)丿\n")
        Saude-=1
        VidaSocial-=2
        Dinheiro+=2
        Fama+=1
        Nota+=1
        print("\nSeus atríbutos:\n\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
       
        
    else:
        limpar()
        print("\n"+Nome2+":")
        imprime_lentamente("  -Não quero professor.\n")
        print("\nRafael: ")
        imprime_lentamente("  -Que pena queria você participando no projeto (⊙﹏⊙✿)\n  -errr...eu esqueci de dizer valia  nota")
        Saude+=1
        VidaSocial+=2
        Dinheiro-=2
        Fama-=1
        Nota-=1
        print("\nSeus atríbutos:\n\nSaúde= ",Saude,"\nVida social= ",VidaSocial,"\nDinheiro= ",Dinheiro,"\nFama= ",Fama,"\nNota= ",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
        
    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    limpar()    
    
    print("Narrador:")
    imprime_lentamente("  -Você estava indo a caminho da aula e encontra seu amigo, Bruno\n")
    print("\nBruno:")
    imprime_lentamente("  -Eai "+Nome2+" você está indo para aula de Cálculo né, que chatice o(╥﹏╥)o ...\n ")
    
    Faculdade2 = str(input("  -Vamos matar a aula?\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade2 == "S":
        limpar()
        print("\n"+Nome2+":")
        imprime_lentamente("  -Bora mano, talvez ela passe atividade...aaah tanto faz\n")
        sleep(1)
        FaculdadeSorte = random.randint(1,2)
        
        if FaculdadeSorte == 1:
            limpar()
            print("Narrador:")
            imprime_lentamente("  -Que sorte não teve nada avaliativo na aula, mas sua professora te viu matando aula...vish\n")
            Saude+=1
            VidaSocial+=2
            Dinheiro=Dinheiro
            Fama-=2
            Nota-=1
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
            print("\n\nSeus atríbutos:\n\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            
        else:
            limpar()
            print("Narrador:")
            print("  -Que azar teve uma atividade avaliativa(>_<)\n")
            Saude+1
            VidaSocial+=2
            Dinheiro=Dinheiro
            Fama-1
            Nota-=2
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
            print("\n\nSeus atríbutos:\n\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            
            if Faculdade1 == "S":
                print("\nNarrador:")
                imprime_lentamente("  -Você escuta seus professores conversando\n")
                print("\nPaulo:")
                imprime_lentamente("  -Hoje o "+Nome2+" matou aula e ainda  perdeu pontos, pois teve uma atividade avaliativa\n")
                print("\nRafael:")
                imprime_lentamente("  -Ele(a) faz parte do projeto que ordeno, quer dizer...fazia...\n")
                print("\nNarrador:")
                imprime_lentamente("  -Seu professor de cálculo comentou com os outros professores...\n  -O professor Rafael decidiu tirar você do projeto extensão\n")
    else:
        limpar()
        print("\n"+Nome2+":")
        imprime_lentamente("  -Vou matar aula não, vai que tem algo avaliativo\n")
        print("\nNarrador:")
        imprime_lentamente("  -Teve uma atividade avaliativa\n")
        print("\nCriador:")
        imprime_lentamente("  -Uau "+Nome2+" você tirou o maximo de pontos, eu vim lhe parabenizar por essa conquista!")
        Saude=Saude
        VidaSocial-=2
        Dinheiro=Dinheiro
        Fama+=1
        Nota+=2
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
        print("\n\nSeus atríbutos:\n\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")

    imprime_lentamente("\nIntervalo de 10 seg para ler\n")

    limpar()
    print("Narrador:")
    imprime_lentamente("  -"+Nome2+" você conheceu um(a) garoto(a) muito legal na aula de fisíca, ele(a) te chama para um encontro vai ir?")
    Faculdade3 = str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade3 == "S":
        limpar()
        print("\nNarrador: ")
        imprime_lentamente("  -UAU...um date perfeito✨(っ◔︣◡◔᷅)っc(◕︣◡◕᷅c)✨, vocês riram muito")
        print("\nCriador:")
        imprime_lentamente("  -Amo um romance ✍(◔◡◔)")
        Saude+=1
        VidaSocial+=1
        Dinheiro-=2
        Fama+=1
        Nota=Nota
        print("\n\nSeus atríbutos:\n\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    else:
        limpar()
        print("\nNarrador:")
        imprime_lentamente("  -Desculpa esfarrapada...você disse que tinha que dar banho em seu cachorro\n")
        print("\nCriador:")
        imprime_lentamente("  -AAh que pena...eu gosto tanto de um romance (ง︡'-'︠)ง")
        Saude-=1
        VidaSocial-=1
        Dinheiro+=1
        Fama-=1
        Nota=Nota
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    limpar()    
    
    print("Narrador:")
    imprime_lentamente("  -"+Nome2+" Chegou o dia de você pagar o aluguel , custa 3 de dinheiro irá pagar?") 
    
    Faculdade4 = str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade4 == "S":
        limpar()
        print("\nNarrador:")
        imprime_lentamente("  -Aluguel pago")
        Saude-=1
        VidaSocial+=1
        Dinheiro-=2
        Fama+=1
        Nota=Nota
        print("\n\nSeus atríbutos\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    else:
        limpar()
        print("\nJorge:")
        imprime_lentamente("  -"+Nome2+" com você não pagou o aluguel esse mês...quero que você saia da MINHA CASA!!")       
        print("\n\nNarrador:")
        imprime_lentamente("  -O dono da casa te pediu para cair fora...e agr?")
        Saude-=1
        VidaSocial-=1
        Dinheiro+=2
        Fama-=2
        Nota=Nota
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
        
        if Faculdade3 == "S":
            imprime_lentamente("Em 10 seg a tela do terminal será apagada\n")
        
            limpar()
            print("\nNarrador:")
            imprime_lentamente("  -Que sorte!!, o seu date no ultimo cénario oferece de compartilhar a casa com você")
            Saude+=1
            VidaSocial+=1
            Dinheiro+=2
            Fama+=1
            Nota+=1
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
            
        else:
            imprime_lentamente("Em 10 seg a tela do terminal será apagada\n")
        
            limpar()
            print("\nNarrador:")
            imprime_lentamente("  -"+Nome2+"você terá que vender algumas coisas preciosas para poder alugar uma nova casa ou pede apoio da faculdade")
            
            Vender=str(input("\nNarrador:\n  -"+Nome2+" ira vender, caso responder não você vai pedir apoio a faculdade \n\nSim=S\nNão=N\n")).upper()
            
            if Vender == "S":
                limpar()
                print("\nNarrador:")
                imprime_lentamente("  -Você recebeu 2 de dinheiro após vender algumas coisas")
                Saude-=1
                VidaSocial-=1
                Dinheiro+=2
                Fama-=1
                Nota-=1
                print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
                print("\nNarrador:")
                imprime_lentamente("  -Você alugou uma casa mais barata, e perdeu 1 de dinheiro")
                
                Dinheiro-=1
                print("Dinheiro=",Dinheiro)
                sleep(3)
                verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
                        
            else:
                limpar()
                print("\nNarrador:\n  -Você pede apoio da escola")
                sleep(2)
                Apoio_Escolar=random.randint(1,2)
                
                if Apoio_Escolar == 1:
                    limpar()
                    print("\nNarrador:")
                    imprime_lentamente("  -Resultado do processo saindo...\n")
                    cronometro(5)
                    imprime_lentamente("  -Você passou no processo seletivo , agora você dorme no dormitorio da faculdade")
                    Saude+=2
                    VidaSocial+=1
                    Dinheiro+=1
                    Fama-=1
                    Nota+=1
                    print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
                    sleep(3)
                    verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
                
                else:
                    limpar()
                    print("\nNarrador:")
                    imprime_lentamente("  -Resultado do processo saindo...")
                    cronometro(5)
                    imprime_lentamente("  -Você não passou no processo seletivo , e logo teve que vender suas coisa e alugar um casa você ganha 1 de dinheiro, mas perde 2")
                    Saude-=2
                    VidaSocial-=1
                    Dinheiro+=1
                    Fama-=1
                    Nota-=1
                    print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
                    Dinheiro-=3
                    print("\n\nNarrador:\n  -Após pagar seu aluguel:\nDinheiro=",Dinheiro)
                    sleep(3)
                    verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    imprime_lentamente("\n\nIntervalo de 10 seg para leitura\n")

    limpar()             
    print("Narrador:")
    imprime_lentamente("  -"+Nome2+" terá um mini curso de robôtica (pago= 2 Dinheiro) na faculdade e você é convidado(a) por um amigo, vai ir?")
    
    Faculdade5 = str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade5 == "S":
            limpar()
            print("\nNarrador:")
            imprime_lentamente("  -Seu professor apreciou seu interesse no curso...")
            imprime_lentamente("\n  -Mas ninguém avisou que era 4 horas seguidas...um curso bem cansativo")
            Saude-=1
            VidaSocial-=1
            Dinheiro-=2
            Fama+=1
            Nota+=2
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    else:
        limpar()
        print("\nNarrador:")
        imprime_lentamente("  -Seu amigo ficou meio triste com sua resposta...")
        Saude+=1
        VidaSocial-=1
        Dinheiro+=2
        Fama-=1
        Nota-=1
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    

    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    limpar()        

    Faculdade6 = str(input("\nNarrador:\n  -Chegando ao final do periódo novamente, dessa vez você terá que fazer um TCC.\n\n  -Escolha um tema:\n> Criar um jogo=CJ\n> Proteínas nas frutas=PF: ")).upper()
    
    if Faculdade6 == "CJ":
            limpar()
            print("Narrador:")
            imprime_lentamente("  -"+Nome2+" parabéns os professores amaram a ideia e o jogo. Você passou...continue sua vida na programação")
            Saude-=1
            VidaSocial-=1
            Dinheiro+=2
            Fama+=2
            Nota+=2
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    else:
        limpar()
        print("Narrador:")
        imprime_lentamente("  -Os professores não gostaram do tema e pediram para você refazer escolha outro tema:")
        
        TCC=str(input("\n\n  -Tradutor de português para libras= TL\n  -Analíse e comparação de DNA= AC\n")).upper()
        
        if TCC == "TL":
            limpar()
            print("Narrador:")
            imprime_lentamente("  -Uauuuu. Muito bom seus profesorres gostaram e você passou.")
            Saude-=1
            VidaSocial-=2
            Dinheiro+=1
            Fama+=1
            Nota+=2
            print("\n\nSeus atríbutos:\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
        
        else:
            limpar()
            print("Narrador:")
            imprime_lentamente("  -Nossa seus professores ficaram admirados com o projeto")
            Saude-=1
            VidaSocial-=2
            Dinheiro+=2
            Fama+=2
            Nota+=2
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    
    limpar()
    
    print("╔╗╔╗╔╗╔══╗╔═╗─╔╗")
    print("║║║║║║╚╣╠╝║║╚╗║║")
    print("║║║║║║─║║─║╔╗╚╝║")
    print("║╚╝╚╝║─║║─║║╚╗║║")
    print("╚╗╔╗╔╝╔╣╠╗║║─║║║")
    print("─╚╝╚╝─╚══╝╚╝─╚═╝")
    print("\n\n\nCriador:")
    imprime_lentamente("  -"+Nome2+" parabéns!!!!!!!. Você venceu o jogo")
    imprime_lentamente("\n\nVocê venceu o modo = FACÌL\n")
    
    print("\nCriador:")
    imprime_lentamente("  -Deseja reniciar voltar ao menu?")
    
    Reniciar1=str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Reniciar1 == "S":
        MenuJogo(Nome)
    
    else:
        limpar()
        print('               ___________      .__  __  .__ ')                                    
        print("               \_   _____/__  __|__|/  |_|__| ____    ____")                       
        print("                |    __)_\  \/  /  \   __\  |/    \  / ___\ ")                      
        print("                |        \>    <|  ||  | |  |   |  \/ /_/  >")                         
        print("                /_______  /__/\_ \__||__| |__|___|  /\___  / /\ /\ /\ /\ /\ /\ /\ ")
        print("                        \/      \/                \//_____/  \/ \/ \/ \/ \/ \/ \/")
        imprime_lentamente("\n\nFIM DE JOGO\n\n")
        Sair(Nome)
    
def JogoNormal(Nome2,Saude,VidaSocial,Dinheiro,Fama,Nota):
    
    limpar()
    pygame.init()

    
   
    print("\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-JOGO COMEÇOU-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n")
    print("\nNarrador:")
    imprime_lentamente("  -"+Nome2+" você está no ultimo período da faculdade de Ciência da Computação, você vai passar por varías situações ao decorrer do jogo\n  -Boa Sorte\n\n  -Agora vamos começar:\n")
    
    cronometro(3)
    limpar()
    
    print("\nNarrador:")
    imprime_lentamente("  -Você encontrou com seu professor (Rafael) no corredor\n")
    print("\nRafael:")
    imprime_lentamente("  -Olá "+Nome2+" eu abri uma vaga em um projeto extensão, você quer participar?")
    
    Faculdade1 = str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade1 == "S":
        limpar()
        print("\n"+Nome2+":")
        imprime_lentamente("  -Sim professor eu aceito, obrigado.\n")
        print("\nRafael:")
        imprime_lentamente("  -A propósito valeu nota!\n")
        print("\nNarrador:")
        imprime_lentamente("  -Okay sua jornada de trabalho começa aqui ヽ(^。^)丿\n")
        Saude-=2
        VidaSocial-=3
        Dinheiro+=3
        Fama+=2
        Nota+=2
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
       
        
    else:
        limpar()
        print("\n"+Nome2+":")
        imprime_lentamente("  -Não quero professor.\n")
        print("\nRafael: ")
        imprime_lentamente("  -Que pena queria você participando no projeto (⊙﹏⊙✿)\n  -errr...eu esqueci de dizer valia nota")
        Saude+=2
        VidaSocial+=3
        Dinheiro-=3
        Fama-=2
        Nota-=2
        print("\n\nSeus atríbutos:\nSaúde= ",Saude,"\nVida social= ",VidaSocial,"\nDinheiro= ",Dinheiro,"\nFama= ",Fama,"\nNota= ",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
        
    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    limpar()    
    
    print("Narrador:")
    imprime_lentamente("  -Você estava indo a caminho da aula e encontra seu amigo, Bruno\n")
    print("\nBruno:")
    imprime_lentamente("  -Eai "+Nome2+" você está indo para aula de Cálculo né, que chatice o(╥﹏╥)o ...\n ")
    
    Faculdade2 = str(input("  -Vamos matar a aula?\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade2 == "S":
        limpar()
        print("\n"+Nome2+":")
        imprime_lentamente("  -Bora mano, talvez ela passe atividade...aaah tanto faz\n")
        sleep(1)
        FaculdadeSorte = random.randint(1,2)
        
        if FaculdadeSorte == 1:
            limpar()
            print("Narrador:")
            imprime_lentamente("  -Que sorte não teve nada avaliativo na aula, mas sua professora te viu matando aula...vish\n")
            Saude+=2
            VidaSocial+=3
            Dinheiro=Dinheiro
            Fama-=3
            Nota-=2
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
            
        else:
            limpar()
            print("Narrador:")
            print("  -Que azar teve uma atividade avaliativa(>_<)\n")
            Saude+2
            VidaSocial+=3
            Dinheiro=Dinheiro
            Fama-2
            Nota-=3
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
            
            if Faculdade1 == "S":
                print("\nNarrador:")
                imprime_lentamente("  -Você escuta seus professores conversando\n")
                print("\nPaulo:")
                imprime_lentamente("  -Hoje o "+Nome2+" matou aula e ainda  perdeu pontos, pois teve uma atividade avaliativa\n")
                print("\nRafael:")
                imprime_lentamente("  -Ele(a) faz parte do projeto que ordeno, quer dizer...fazia...\n")
                print("\nNarrador:")
                imprime_lentamente("  -Seu professor de cálculo comentou com os outros professores...\n  -O professor Rafael decidiu tirar você do projeto extensão\n")
    else:
        limpar()
        print("\n"+Nome2+":")
        imprime_lentamente("  -Vou matar aula não, vai que tem algo avaliativo\n")
        print("\nNarrador:")
        imprime_lentamente("  -Teve uma atividade avaliativa\n")
        print("\nCriador:")
        imprime_lentamente("  -Uau "+Nome2+" você tirou o maximo de pontos, eu vim lhe parabenizar por essa conquista!")
        Saude=Saude
        VidaSocial-=3
        Dinheiro=Dinheiro
        Fama+=2
        Nota+=3
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)

    imprime_lentamente("\nIntervalo de 10 seg para ler\n")

    limpar()
    print("Narrador:")
    imprime_lentamente("  -"+Nome2+" você conheceu um(a) garoto(a) muito legal na aula de fisíca, ele(a) te chama para um encontro vai ir?")
    
    Faculdade3 = str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade3 == "S":
        limpar()
        print("\nNarrador: ")
        imprime_lentamente("  -UAU...um date perfeito✨(っ◔︣◡◔᷅)っc(◕︣◡◕᷅c)✨, vocês riram muito")
        print("\nCriador:")
        imprime_lentamente("  -Amo um romance ✍(◔◡◔)")
        Saude+=2
        VidaSocial+=2
        Dinheiro-=3
        Fama+=2
        Nota=Nota
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    else:
        limpar()
        print("\nNarrador:")
        imprime_lentamente("  -Desculpa esfarrapada...você disse que tinha que dar banho em seu cachorro\n")
        print("\nCriador:")
        imprime_lentamente("  -AAh que pena...eu gosto tanto de um romance (ง︡'-'︠)ง")
        Saude-=2
        VidaSocial-=2
        Dinheiro+=2
        Fama-=2
        Nota=Nota
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    
    limpar()    
    
    print("Narrador:")
    imprime_lentamente("  -"+Nome2+" Chegou o dia de você pagar o aluguel , custa 3 de dinheiro irá pagar?") 
    
    Faculdade4 = str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade4 == "S":
        limpar()
        print("\nNarrador:")
        imprime_lentamente("  -Aluguel pago")
        Saude-=2
        VidaSocial+=2
        Dinheiro-=3
        Fama+=2
        Nota=Nota
        print("\n\nSeus atríbutos\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    else:
        limpar()
        print("\nJorge:")
        imprime_lentamente("  -"+Nome2+" com você não pagou o aluguel esse mês...quero que você saia da MINHA CASA!!")       
        print("\n\nNarrador:")
        imprime_lentamente("  -O dono da casa te pediu para cair fora...e agr?")
        Saude-=2
        VidaSocial-=2
        Dinheiro+=3
        Fama-=3
        Nota=Nota
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
        
        if Faculdade3 == "S":
            imprime_lentamente("Em 10 seg a tela do terminal será apagada\n")
        
            limpar()
            print("\nNarrador:")
            imprime_lentamente("  -Que sorte!!, o seu date no ultimo cénario oferece de compartilhar a casa com você")
            Saude+=2
            VidaSocial+=2
            Dinheiro+=3
            Fama+=2
            Nota+=2
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
            
        else:
            imprime_lentamente("Em 10 seg a tela do terminal será apagada\n")
        
            limpar()
            print("\nNarrador:")
            imprime_lentamente("  -"+Nome2+" você terá que vender algumas coisas preciosas para poder alugar uma nova casa ou pede apoio da faculdade")
            
            Vender=str(input("\nNarrador:\n  -"+Nome2+" ira vender, caso responder não você vai pedir apoio a faculdade \n\nSim=S\nNão=N\n")).upper()
            
            if Vender == "S":
                limpar()
                print("\nNarrador:")
                imprime_lentamente("  -Você recebeu 3 de dinheiro após vender algumas coisas")
                Saude-=2
                VidaSocial-=2
                Dinheiro+=3
                Fama-=2
                Nota-=2
                print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
                print("\nNarrador:")
                imprime_lentamente("  -Você alugou uma casa mais barata, e perdeu 2 de dinheiro")
                Dinheiro-=2
                print("Dinheiro=",Dinheiro)
                sleep(3)
                verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
                        
            else:
                limpar()
                print("\nNarrador:\n  -Você pede apoio da escola")
                sleep(2)
                Apoio_Escolar=random.randint(1,2)
                
                if Apoio_Escolar == 1:
                    limpar()
                    print("\nNarrador:")
                    imprime_lentamente("  -Resultado do processo saindo...\n")
                    cronometro(5)
                    imprime_lentamente("  -Você passou no processo seletivo , agora você dorme no dormitorio da faculdade")
                    Saude+=3
                    VidaSocial+=2
                    Dinheiro+=2
                    Fama-=2
                    Nota+=2
                    print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
                    sleep(3)
                    verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
                
                else:
                    limpar()
                    print("\nNarrador:")
                    imprime_lentamente("  -Resultado do processo saindo...")
                    cronometro(5)
                    imprime_lentamente("  -Você não passou no processo seletivo , e logo teve que vender suas coisa e alugar um casa você ganha 1 de dinheiro, mas perde 2")
                    Saude-=3
                    VidaSocial-=2
                    Dinheiro+=2
                    Fama-=2
                    Nota-=2
                    print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
                    Dinheiro-=3
                    print("\n\nNarrador:\n  -Após pagar seu aluguel:\nDinheiro=",Dinheiro)
                    sleep(3)
                    verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    imprime_lentamente("\n\nIntervalo de 10 seg para leitura\n")

    limpar()             
    print("Narrador:")
    imprime_lentamente("  -"+Nome2+" terá um mini curso de robôtica (pago= 2 Dinheiro) na faculdade e você é convidado(a) por um amigo, vai ir?")
    
    Faculdade5 = str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade5 == "S":
            limpar()
            print("\nNarrador:")
            imprime_lentamente("  -Seu professor apreciou seu interesse no curso...\ns")
            imprime_lentamente("\n  -Mas ninguém avisou que era 4 horas seguidas...um curso bem cansativo")
            Saude-=2
            VidaSocial-=2
            Dinheiro-=3
            Fama+=2
            Nota+=3
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    else:
        limpar()
        print("\nNarrador:")
        imprime_lentamente("  -Seu amigo ficou meio triste com sua resposta...")
        Saude+=2
        VidaSocial-=2
        Dinheiro+=3
        Fama-=2
        Nota-=2
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    limpar()       
    
    print("Narrador:")
    imprime_lentamente("  -Falta apenas 10 minutos para aula começar, mas você está morrendo de fome")
    
    Faculdade6 = str(input("  -Deseja ir a cantina?\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade6 == "S":
        
        Atraso= random.randint(1,2)
        
        if Atraso == 1:
            limpar()
            print("Narrador:")
            imprime_lentamente("  -Que sorte, "+Nome2+", você chegou a tempo na sala")
            Saude+=2
            VidaSocial=VidaSocial
            Dinheiro-=2
            Fama=Fama
            Nota+=2
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)

        else:
            limpar()
            print("Narrador:")
            imprime_lentamente("  -Que azar, "+Nome2+" você chegou atrasado na aula, seu professor deixou você entrar na sala mesmo assim\n")
            Saude+=2
            VidaSocial=VidaSocial
            Dinheiro-=2
            Fama-=2
            Nota=Nota
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    else:
        limpar()
        print("Narrador:")
        imprime_lentamente("  -Você chego sem atraso na sala, mas com a barriga roncando") 
        Saude-=2
        VidaSocial=VidaSocial
        Dinheiro+=2
        Fama+=2
        Nota+=2
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)



    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    limpar()        

    Faculdade7 = str(input("\nNarrador:\n   -Chegando ao final do periódo novamente, dessa vez você terá que fazer um TCC.\n\n  -Escolha um tema:\n> Criar um jogo=CJ\n> Proteínas nas frutas=PF: ")).upper()
    
    
    if Faculdade7 == "CJ":
            limpar()
            print("Narrador:")
            imprime_lentamente("  -"+Nome2+" parabéns os professores amaram a ideia e o jogo. Você passou...continue sua vida na programação")
            Saude-=2
            VidaSocial-=2
            Dinheiro+=3
            Fama+=3
            Nota+=3
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    else:
        limpar()
        print("Narrador:")
        imprime_lentamente("  -Os professores não gostaram do tema e pediram para você refazer escolha outro tema:")
        
        TCC=str(input("\n\n  -Tradutor de português para libras= TL\n  -Analíse e comparação de DNA= AC\n")).upper()
        
        if TCC == "TL":
            limpar()
            print("Narrador:")
            imprime_lentamente("  -Uauuuu. Muito bom seus profesorres gostaram e você passou.")
            Saude-=2
            VidaSocial-=3
            Dinheiro+=2
            Fama+=2
            Nota+=3
            print("\n\nSeus atríbutos:\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
        
        else:
            limpar()
            print("Narrador:")
            imprime_lentamente("  -Nossa seus professores ficaram admirados com o projeto")
            Saude-=2
            VidaSocial-=3
            Dinheiro+=3
            Fama+=3
            Nota+=3
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    
    
    print("╔╗╔╗╔╗╔══╗╔═╗─╔╗")
    print("║║║║║║╚╣╠╝║║╚╗║║")
    print("║║║║║║─║║─║╔╗╚╝║")
    print("║╚╝╚╝║─║║─║║╚╗║║")
    print("╚╗╔╗╔╝╔╣╠╗║║─║║║")
    print("─╚╝╚╝─╚══╝╚╝─╚═╝")
    print("\n\n\nCriador:")
    imprime_lentamente("  -"+Nome2+" parabéns!!!!!!!. Você venceu o jogo")
    imprime_lentamente("\n\nVocê venceu o modo = NORMAL\n")
    
    print("\nCriador:")
    imprime_lentamente("  -Deseja reniciar voltar ao menu?")
    
    Reniciar1=str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Reniciar1 == "S":
        MenuJogo(Nome)
    
    else:
        limpar()
        print('               ___________      .__  __  .__ ')                                    
        print("               \_   _____/__  __|__|/  |_|__| ____    ____")                       
        print("                |    __)_\  \/  /  \   __\  |/    \  / ___\ ")                      
        print("                |        \>    <|  ||  | |  |   |  \/ /_/  >")                         
        print("                /_______  /__/\_ \__||__| |__|___|  /\___  / /\ /\ /\ /\ /\ /\ /\ ")
        print("                        \/      \/                \//_____/  \/ \/ \/ \/ \/ \/ \/")
        imprime_lentamente("\n\nFIM DE JOGO\n\n")
        Sair(Nome)

def JogoDificil(Nome2,Saude,VidaSocial,Dinheiro,Fama,Nota):
    
    limpar()
    pygame.init()
    
    
    print("\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-JOGO COMEÇOU-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n")
    print("\nNarrador:")
    imprime_lentamente("  -"+Nome2+" você está no ultimo período da faculdade de Ciência da Computação, você vai passar por varías situações ao decorrer do jogo\n  -Boa Sorte\n\n  -Agora vamos começar:\n")
    
    cronometro(3)
    limpar()
   
    print("\nNarrador:")
    imprime_lentamente("  -Você encontrou com seu professor (Rafael) no corredor\n")
    print("\nRafael:")
    imprime_lentamente("  -Olá "+Nome2+" eu abri uma vaga em um projeto extensão, você quer participar?")
    
    Faculdade1 = str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade1 == "S":
        limpar()
        print("\n"+Nome2+":")
        imprime_lentamente("  -Sim professor eu aceito, obrigado.\n")
        print("\nRafael:")
        imprime_lentamente("  -A propósito valeu nota!\n")
        print("\nNarrador:")
        imprime_lentamente("  -Okay sua jornada de trabalho começa aqui ヽ(^。^)丿\n")
        Saude-=3
        VidaSocial-=4
        Dinheiro+=4
        Fama+=3
        Nota+=3
        print("\nSeus atríbutos:\n\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
       
        
    else:
        limpar()
        print("\n"+Nome2+":")
        imprime_lentamente("  -Não quero professor.\n")
        print("\nRafael: ")
        imprime_lentamente("  -Que pena queria você participando no projeto (⊙﹏⊙✿)\n  -errr...eu esqueci de dizer valia nota")
        Saude+=3
        VidaSocial+=4
        Dinheiro-=4
        Fama-=3
        Nota-=3
        print("\nSeus atríbutos:\n\nSaúde= ",Saude,"\nVida social= ",VidaSocial,"\nDinheiro= ",Dinheiro,"\nFama= ",Fama,"\nNota= ",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
        
    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    limpar()    
    
    print("Narrador:")
    imprime_lentamente("  -Você estava indo a caminho da aula e encontra seu amigo, Bruno\n")
    print("\nBruno:")
    imprime_lentamente("  -Eai "+Nome2+" você está indo para aula de Cálculo né, que chatice o(╥﹏╥)o ...\n ")
    
    Faculdade2 = str(input("  -Vamos matar a aula?\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade2 == "S":
        limpar()
        print("\n"+Nome2+":")
        imprime_lentamente("  -Bora mano, talvez ela passe atividade...aaah tanto faz\n")
        sleep(1)
        FaculdadeSorte = random.randint(1,2)
        
        if FaculdadeSorte == 1:
            limpar()
            print("Narrador:")
            imprime_lentamente("  -Que sorte não teve nada avaliativo na aula, mas sua professora te viu matando aula...vish\n")
            Saude+=3
            VidaSocial+=4
            Dinheiro=Dinheiro
            Fama-=4
            Nota-=3
            print("\n\nSeus atríbutos:\n\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
            
        else:
            limpar()
            print("Narrador:")
            print("  -Que azar teve uma atividade avaliativa(>_<)\n")
            Saude+3
            VidaSocial+=4
            Dinheiro=Dinheiro
            Fama-3
            Nota-=4
            print("\n\nSeus atríbutos:\n\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
            
            if Faculdade1 == "S":
                print("\nNarrador:")
                imprime_lentamente("  -Você escuta seus professores conversando\n")
                print("\nPaulo:")
                imprime_lentamente("  -Hoje o "+Nome2+" matou aula e ainda  perdeu pontos, pois teve uma atividade avaliativa\n")
                print("\nRafael:")
                imprime_lentamente("  -Ele(a) faz parte do projeto que ordeno, quer dizer...fazia...\n")
                print("\nNarrador:")
                imprime_lentamente("  -Seu professor de cálculo comentou com os outros professores...\n  -O professor Rafael decidiu tirar você do projeto extensão\n")
    else:
        limpar()
        print("\n"+Nome2+":")
        imprime_lentamente("  -Vou matar aula não, vai que tem algo avaliativo\n")
        print("\nNarrador:")
        imprime_lentamente("  -Teve uma atividade avaliativa\n")
        print("\nCriador:")
        imprime_lentamente("  -Uau "+Nome2+" você tirou o maximo de pontos, eu vim lhe parabenizar por essa conquista!")
        Saude=Saude
        VidaSocial-=4
        Dinheiro=Dinheiro
        Fama+=3
        Nota+=4
        print("\n\nSeus atríbutos:\n\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)

    imprime_lentamente("\nIntervalo de 10 seg para ler\n")

    limpar()
    print("Narrador:")
    imprime_lentamente("  -"+Nome2+" você conheceu um(a) garoto(a) muito legal na aula de fisíca, ele(a) te chama para um encontro vai ir?")
    
    Faculdade3 = str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade3 == "S":
        limpar()
        print("\nNarrador: ")
        imprime_lentamente("  -UAU...um date perfeito✨(っ◔︣◡◔᷅)っc(◕︣◡◕᷅c)✨, vocês riram muito")
        print("\nCriador:")
        imprime_lentamente("  -Amo um romance ✍(◔◡◔)")
        Saude+=3
        VidaSocial+=3
        Dinheiro-=4
        Fama+=3
        Nota=Nota
        print("\n\nSeus atríbutos:\n\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    else:
        limpar()
        print("\nNarrador:")
        imprime_lentamente("  -Desculpa esfarrapada...você disse que tinha que dar banho em seu cachorro\n")
        print("\nCriador:")
        imprime_lentamente("  -AAh que pena...eu gosto tanto de um romance (ง︡'-'︠)ง")
        Saude-=3
        VidaSocial-=3
        Dinheiro+=3
        Fama-=3
        Nota=Nota
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    limpar()    
    
    print("Narrador:")
    imprime_lentamente("  -"+Nome2+" Chegou o dia de você pagar o aluguel , custa 3 de dinheiro irá pagar?") 
    
    Faculdade4 = str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade4 == "S":
        limpar()
        print("\nNarrador:")
        imprime_lentamente("  -Aluguel pago")
        Saude-=3
        VidaSocial+=3
        Dinheiro-=4
        Fama+=3
        Nota=Nota
        print("\n\nSeus atríbutos\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    else:
        limpar()
        print("\nJorge:")
        imprime_lentamente("  -"+Nome2+" com você não pagou o aluguel esse mês...quero que você saia da MINHA CASA!!")       
        print("\n\nNarrador:")
        imprime_lentamente("  -O dono da casa te pediu para cair fora...e agr?")
        Saude-=3
        VidaSocial-=3
        Dinheiro+=4
        Fama-=4
        Nota=Nota
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
        
        if Faculdade3 == "S":
            imprime_lentamente("Em 10 seg a tela do terminal será apagada\n")
        
            limpar()
            print("\nNarrador:")
            imprime_lentamente("  -Que sorte!!, o seu date no ultimo cénario oferece de compartilhar a casa com você")
            Saude+=3
            VidaSocial+=3
            Dinheiro+=4
            Fama+=3
            Nota+=3
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
            
        else:
            imprime_lentamente("Em 10 seg a tela do terminal será apagada\n")
        
            limpar()
            print("\nNarrador:")
            imprime_lentamente("  -"+Nome2+"você terá que vender algumas coisas preciosas para poder alugar uma nova casa ou pede apoio da faculdade")
            
            Vender=str(input("\nNarrador:\n  -"+Nome2+" ira vender, caso responder não você vai pedir apoio a faculdade \n\nSim=S\nNão=N\n")).upper()
            
            if Vender == "S":
                limpar()
                print("\nNarrador:")
                imprime_lentamente("  -Você recebeu 4 de dinheiro após vender algumas coisas")
                Saude-=3
                VidaSocial-=3
                Dinheiro+=4
                Fama-=3
                Nota-=3
                print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
                print("\nNarrador:")
                imprime_lentamente("  -Você alugou uma casa mais barata, e perdeu 3 de dinheiro")
                Dinheiro-=3
                print("Dinheiro=",Dinheiro)
                sleep(3)
                verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
                        
            else:
                limpar()
                print("\nNarrador:\n  -Você pede apoio da escola")
                sleep(2)
                Apoio_Escolar=random.randint(1,2)
                
                if Apoio_Escolar == 1:
                    limpar()
                    print("\nNarrador:")
                    imprime_lentamente("  -Resultado do processo saindo...\n")
                    cronometro(5)
                    imprime_lentamente("  -Você passou no processo seletivo , agora você dorme no dormitorio da faculdade")
                    Saude+=4
                    VidaSocial+=3
                    Dinheiro+=3
                    Fama-=3
                    Nota+=3
                    print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
                    sleep(3)
                    verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
                
                else:
                    limpar()
                    print("\nNarrador:")
                    imprime_lentamente("  -Resultado do processo saindo...")
                    cronometro(5)
                    imprime_lentamente("  -Você não passou no processo seletivo , e logo teve que vender suas coisa e alugar um casa você ganha 1 de dinheiro, mas perde 2")
                    Saude-=4
                    VidaSocial-=3
                    Dinheiro+=3
                    Fama-=3
                    Nota-=3
                    print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
                    Dinheiro-=4
                    print("\n\nNarrador:\n  -Após pagar seu aluguel:\nDinheiro=",Dinheiro)
                    sleep(3)
                    verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    imprime_lentamente("\n\nIntervalo de 10 seg para leitura\n")

    limpar()             
    print("Narrador:")
    imprime_lentamente("  -"+Nome2+" terá um mini curso de robôtica (pago= 2 Dinheiro) na faculdade e você é convidado(a) por um amigo, vai ir?")
    
    Faculdade5 = str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade5 == "S":
            limpar()
            print("\nNarrador:")
            imprime_lentamente("  -Seu professor apreciou seu interesse no curso...")
            imprime_lentamente("\n  -Mas ninguém avisou que era 4 horas seguidas...um curso bem cansativo")
            Saude-=3
            VidaSocial-=3
            Dinheiro-=4
            Fama+=3
            Nota+=3
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    else:
        limpar()
        print("\nNarrador:")
        imprime_lentamente("  -Seu amigo ficou meio triste com sua resposta...")
        Saude+=3
        VidaSocial-=3
        Dinheiro+=4
        Fama-=3
        Nota-=3
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    limpar()       
    
    print("Narrador:")
    imprime_lentamente("  -Falta apenas 10 minutos para aula começar, mas você está morrendo de fome")
    
    Faculdade6 = str(input("  -Deseja ir a cantina?\n\nSim=S\nNão=N\n")).upper()
    
    if Faculdade6 == "S":
        
        Atraso= random.randint(1,2)
        
        if Atraso == 1:
            limpar()
            print("Narrador:")
            imprime_lentamente("  -Que sorte, "+Nome2+", você chegou a tempo na sala")
            Saude+=3
            VidaSocial=VidaSocial
            Dinheiro-=3
            Fama=Fama
            Nota+=3
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)

        else:
            limpar()
            ProfSorte=random.randint(1,2)
            if ProfSorte == 1:
                print("Narrador:")
                imprime_lentamente("  -Que azar, "+Nome2+" você chegou atrasado na aula, seu professor deixou você entrar na sala mesmo assim\n")
                Saude+=3
                VidaSocial=VidaSocial
                Dinheiro-=3
                Fama-=3
                Nota=Nota
                print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
                sleep(3)
                verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
            
            else:
                print("Narrador:")
                imprime_lentamente("  -Que azar, "+Nome2+" você chegou atrasado na aula, seu professor  não deixou você entrar na sala \n")
                Saude-=3
                VidaSocial=VidaSocial
                Dinheiro-=3
                Fama-=4
                Nota=Nota
                print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
                sleep(3)
                verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    else:
        limpar()
        print("Narrador:")
        imprime_lentamente("  -Você chego sem atraso na sala, mas com a barriga roncando") 
        Saude-=3
        VidaSocial=VidaSocial
        Dinheiro+=3
        Fama+=3
        Nota+=3
        print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
        sleep(3)
        verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)



    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    limpar()        

    Faculdade7 = str(input("\nNarrador:\n  -Chegando ao final do periódo novamente, dessa vez você terá que fazer um TCC.\n\n  -Escolha um tema:\n> Criar um jogo=CJ\n> Proteínas nas frutas=PF: ")).upper()
    
    if Faculdade7 == "CJ":
            limpar()
            print("Narrador:")
            imprime_lentamente("  -"+Nome2+" parabéns os professores amaram a ideia e o jogo. Você passou...continue sua vida na programação")
            Saude-=3
            VidaSocial-=3
            Dinheiro+=4
            Fama+=4
            Nota+=4
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    else:
        limpar()
        print("Narrador:")
        imprime_lentamente("  -Os professores não gostaram do tema e pediram para você refazer escolha outro tema:")
        
        TCC=str(input("\n\n  -Tradutor de português para libras= TL\n  -Analíse e comparação de DNA= AC\n")).upper()
        
        if TCC == "TL":
            limpar()
            print("Narrador:")
            imprime_lentamente("  -Uauuuu. Muito bom seus profesorres gostaram e você passou.")
            Saude-=3
            VidaSocial-=4
            Dinheiro+=3
            Fama+=3
            Nota+=4
            print("\n\nSeus atríbutos:\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
        
        else:
            limpar()
            print("Narrador:")
            imprime_lentamente("  -Nossa seus professores ficaram admirados com o projeto")
            Saude-=3
            VidaSocial-=4
            Dinheiro+=4
            Fama+=4
            Nota+=4
            print("\n\nSeus atríbutos:\nSaúde=",Saude,"\nVida social=",VidaSocial,"\nDinheiro=",Dinheiro,"\nFama=",Fama,"\nNota=",Nota,"\n")
            sleep(3)
            verificar_game_over(Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    imprime_lentamente("\n\nIntervalo de 10 seg para ler\n")

    
    limpar()

    print("╔╗╔╗╔╗╔══╗╔═╗─╔╗")
    print("║║║║║║╚╣╠╝║║╚╗║║")
    print("║║║║║║─║║─║╔╗╚╝║")
    print("║╚╝╚╝║─║║─║║╚╗║║")
    print("╚╗╔╗╔╝╔╣╠╗║║─║║║")
    print("─╚╝╚╝─╚══╝╚╝─╚═╝")
    print("\n\n\nCriador:")
    imprime_lentamente("  -"+Nome2+" parabéns!!!!!!!. Você venceu o jogo")
    imprime_lentamente("\n\nVocê venceu o modo = DIFÌCIL\n")
    
    print("\nCriador:")
    imprime_lentamente("  -Deseja reniciar voltar ao menu?")
    
    Reniciar1=str(input("\n\nSim=S\nNão=N\n")).upper()
    
    if Reniciar1 == "S":
        MenuJogo(Nome)
    
    else:
        limpar()
        print('               ___________      .__  __  .__ ')                                    
        print("               \_   _____/__  __|__|/  |_|__| ____    ____")                       
        print("                |    __)_\  \/  /  \   __\  |/    \  / ___\ ")                      
        print("                |        \>    <|  ||  | |  |   |  \/ /_/  >")                         
        print("                /_______  /__/\_ \__||__| |__|___|  /\___  / /\ /\ /\ /\ /\ /\ /\ ")
        print("                        \/      \/                \//_____/  \/ \/ \/ \/ \/ \/ \/")
        imprime_lentamente("\n\nFIM DE JOGO\n\n")
        Sair(Nome)
            
def Regras(Nome2):
    limpar()
    print("\nCriador:")
    imprime_lentamente("  -"+Nome2+" esse jogo representa a vida de um programador na faculdade\n  -Você terá 5 atributos basícos:\n")
    
    print("\n   ATRÍBUTOS:\n~~~~~~~~~~~~~~~~")
    imprime_lentamente("Nota          10\nSaúde         10\nVida social   10\nFama          10\nDinheiro      10\n")
    print("~~~~~~~~~~~~~~~~\n")
    
    print("\n                   REGRAS:\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    imprime_lentamente("Todos os atributos começam no máximo, ou seja = 10.\nSe caso algum deles chegarem a 0 você perde o jogo.\nSuas decisões interferem nos pontos, Bom jogo.")
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
   
    print("Intervalo de 10 seg para leitura")

    limpar()
    print("Criador:")
    imprime_lentamente("  -Agora que você conhece as regras vamos lá:\n")
    IniciarJogo(Nome2)
    
def IniciarJogo(Nome2):
    limpar()
    
    print("\n              MODOS DE JOGO\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nFacíl=F(perde entre 1 a 2 pontos de atribútos)\nNormal=N(perde entre 2 a 3 pontos de atribútos)\nDifícil=D(perde entre 3 a 4 pontos de atribútos)\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    
    modo_jogo=str(input("\nCriador:\n  -Escolha o modo que você deseja (F/N/D):\n\n"+Nome2+":\n  -")).upper()
    
    if modo_jogo == "F":
        limpar()
        print("\nNarrador:")  
        imprime_lentamente("  -Você escolheu modo de jogo facíl\n  -Eu(Narrador) ire lhe acompanhar durante essa aventura\n")
        cronometro(5)
        JogoFacil(Nome2,Saude,VidaSocial,Dinheiro,Fama,Nota) 
    
    if modo_jogo == "N":
        limpar()
        print("\nNarrador:\n  -Você escolheu modo de jogo normal\n  -Eu(Narrador) ire lhe acompanhar durante essa aventura\n")
        cronometro(5)
        JogoNormal(Nome2,Saude,VidaSocial,Dinheiro,Fama,Nota)
    
    if modo_jogo == "D":
        print("\nNarrador:\n  -Você escolheu modo de jogo difícil\n  -Eu(Narrador) ire lhe acompanhar durante essa aventura\n")
        cronometro(5)
        JogoDificil(Nome2,Saude,VidaSocial,Dinheiro,Fama,Nota)

  
        
def Creditos(Nome):
    limpar()
    print("Criador:")
    imprime_lentamente("  -"+Nome+" agradecemos o interesse em nosso trabalho S2\n  -Os programadores desse jogo foram:\n  -Aline(no caso eu Criador)\n  -Com ajuda do monitor Wekisley\n")
    sleep(0.5)
    desejo=str(input("\nCriador:\n       -Deseja voltar ao menu? \n\nSim=S\nNão=N\n")).upper()
    if desejo == "S":
        limpar()
        MenuJogo(Nome)
    else:
        limpar()
        print("\nCriador:\n  -Tcahuziin ʕ•́ᴥ•̀ʔっ♡")
  

               
def Sair(Nome):
        limpar()
        print("Criador:")
        imprime_lentamente("  -"+Nome+" tchauzinho,Volte sempre")

    
def NomeJogo(Nome):
    imprime_lentamente("  -"+Nome+" qual será seu nome no jogo:\n")
    MudarNome=str(input("  -"))
    Nome2=MudarNome
    imprime_lentamente("  -"+Nome+" você deseja ver as regras? \n")
    Regra=str(input("\n\nSim=S\nNão=N\n")).upper()
    if Regra =="S":
        Regras(Nome2)
    if Regra == "N":
        IniciarJogo(Nome2)
    
        

    
def MenuJogo(Nome):
    limpar()
    print("\n       MENU\n-=-=-=-=-=-=-=-=-=-=\n1-Iniciar\n2-Créditos\n3-Sair\n-=-=-=-=-=-=-=-=-=-=\n")
    print("Criador:")
    imprime_lentamente("\n  -"+Nome+" qual você escolhe?\n")
    
    Escolha=int(input("  -"))

    if Escolha == 1:
       NomeJogo(Nome)
       
    if Escolha == 2:
        Creditos(Nome)
        
    if Escolha == 3:
        limpar()
        print("Criador:")
        imprime_lentamente("  -"+Nome+" certeza que deseja sair? ")
        Desejo=str(input("\n\nSim=S\nNão=N\n  -")).upper()
        
        if Desejo == "S":
            Sair(Nome)
            
        else:
            limpar()
            print("\nCriador:\n  -",Nome,"que bom que decidiu ficar vamos continuar ʕ•́ᴥ•̀ʔっ")
            MenuJogo(Nome)
    else:
        print("Numero invalido")
        MenuJogo(Nome)
        
MenuJogo(Nome)
