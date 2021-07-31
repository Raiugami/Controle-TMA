import time

print("\n -=- -=- -=- -=- -=- -=- -=- CONTROLE DE TMA -=- -=- -=- -=- -=- -=- -=- \n")

while True:

    arquivo = open("TMA.txt", "a")
    operacao = int(input(''' Escolha a operação:  
    
    [1] Aliança
    [2] Banco Pan
    [3] Bradesco Affinity
    [4] Conectcar
    [5] CTF
    [6] ENEL - RJ
    [7] Intermédica PME / Interodonto IOD
    [8] Kroton
    [9] Lenovo
    [10] Marisa
    [11] Motorola
    [12] OI
    [13] PASA
    [14] Sem Parar
    [15] Shell
    [16] Unimed - RJ
    [17] Via Varejo
    [18] VIVO
    [19] White Martins 
    
    informe aqui:  '''))

    if operacao == 1:
        print("Operação : Aliança")
        arquivo.write("\nOperação : Aliança\n")
    elif operacao == 2:
        print("Operação : Banco PAN")
        arquivo.write("\nOperação : Banco PAN\n")
    elif operacao == 3:
        print("Operação : Bradesco Affinity")
        arquivo.write("\nOperação : Bradesco Affinity\n")
    elif operacao == 4:
        print("Operação : Conectar")
        arquivo.write("\nOperação : Conectar\n")
    elif operacao == 5:
        print("Operação : CTF")
        arquivo.write("\nOperação : CTF\n")
    elif operacao == 6:
        print("Operação : ENEL - RJ")
        arquivo.write("\nOperação : ENEL - RJ\n")
    elif operacao == 7:
        print("Operação : Intermédica PME / Interodonto IOD")
        arquivo.write("\nOperação : Intermédica PME / Interodonto IOD\n")
    elif operacao == 8:
        print("Operação : Kroton")
        arquivo.write("\nOperação : Kroton\n")
    elif operacao == 9:
        print("Operação : Lenovo")
        arquivo.write("\nOperação : Lenovo\n")
    elif operacao == 10:
        print("Operação : Marisa ")
        arquivo.write("\nOperação : Marisa\n ")
    elif operacao == 11:
        print("Operação : Motorola")
        arquivo.write("\nOperação : Motorola\n")
    elif operacao == 12:
        print("Operação : OI ")
        arquivo.write("\nOperação : OI\n ")
    elif operacao == 13:
        print("Operação : PASA ")
        arquivo.write("\nOperação : PASA\n ")
    elif operacao == 14:
        print("Operação : Sem Parar")
        arquivo.write("\nOperação : Sem Parar\n")
    elif operacao == 15:
        print("Operação : Shell")
        arquivo.write("\nOperação : Shell\n")
    elif operacao == 16:
        print("Operação : Unimed - RJ")
        arquivo.write("\nOperação : Unimed - RJ\n")
    elif operacao == 17:
        print("Operação : Via Varejo")
        arquivo.write("\nOperação : Via Varejo\n")
    elif operacao == 18:
        print("Operação :VIVO")
        arquivo.write("\nOperação :VIVO\n")
    elif operacao == 19:
        print("Operação :White Martins")
        arquivo.write("\nOperação :White Martins\n")
    else:
        print("Nenhuma operação encontrada :(")

    colaborador = str(input('\nInforme o protocolo e o nome do colaborador: '))
    arquivo.write("Colaborador: {}\n".format(colaborador))

    analista = int(input('''Escolha o analista responsavel: 
    [1] Antônio Carlos Souza Matos
    [2] Beatriz Teixeira Rosa dos Santos
    [3] Daniel Pinto dos Santos Silva
    [4] Danilo Henrique da Silva
    [5] Diogo Farias de Luna
    [6] Edson Sebastião da Cruz Reis
    [7] Felipe Bonfim da Costa   
    [8] Felipe Rodrigues de Melo
    [9] Fernanda Bandeira de Souza
    [10] Gabriel Antonio do Espirito Santo de Aguiar
    [11] Gilmar Batista da Silva
    [12] Giovanna Santos Fonseca
    [13] Guilherme Alvarez Barboza
    [14] Iago Leal do Nascimento
    [15] Victor Mariano Rodrigues de Moura
    [16] Jefferson Vieira de Melo
    [17] Jefferson Vinicius Correa dos Santos
    [18] Jéssica Pellegrini Borges
    [19] Joyce de Jesus da Silva
    [20] Lucas Alexandre Brito
    [21] Matheus Cruz Alves
    [22] Paulo Machado
    [23] Caique Rodrigues Terrone
    [24] Rodolfo Marcel Barros e Silva
    [25] Rodolfo Vilella Alves
    [26] Rodrigo Oliveira Correia
    [27] Thatiane Alexandra da Silva
    
    Informe o numero corresponde aqui:  '''))

    if analista == 1:
        print("Analista responsavel: Antônio Carlos Souza Matos")
        arquivo.write("Analista responsavel: Antônio Carlos Souza Matos\n")
    elif analista == 2:
        print("Analista responsavel: Beatriz Teixeira Rosa dos Santos")
        arquivo.write("Analista responsavel: Beatriz Teixeira Rosa dos Santos\n")
    elif analista == 3:
        print("Analista responsavel: Daniel Pinto dos Santos Silva")
        arquivo.write("Analista responsavel: Daniel Pinto dos Santos Silva\n")
    elif analista == 4:
        print("Analista responsavel: Danilo Henrique da Silva")
        arquivo.write("Analista responsavel: Danilo Henrique da Silva\n")
    elif analista == 5:
        print("Analista responsavel: Diogo Farias de Luna")
        arquivo.write("Analista responsavel: Diogo Farias de Luna\n")
    elif analista == 6:
        print("Analista responsavel: Edson Sebastião da Cruz Reis")
        arquivo.write("Analista responsavel: Edson Sebastião da Cruz Reis\n")
    elif analista == 7:
        print("Analista responsavel: Felipe Bonfim da Costa")
        arquivo.write("Analista responsavel: Felipe Bonfim da Costa\n")
    elif analista == 8:
        print("Analista responsavel: Felipe Rodrigues de Melo")
        arquivo.write("Analista responsavel: Felipe Rodrigues de Melo\n")
    elif analista == 9:
        print("Analista responsavel: Fernanda Bandeira de Souza")
        arquivo.write("Analista responsavel: Fernanda Bandeira de Souza\n")
    elif analista == 10:
        print("Analista responsavel: Gabriel Antonio do Espirito Santo de Aguiar")
        arquivo.write("Analista responsavel: Gabriel Antonio do Espirito Santo de Aguiar\n")
    elif analista == 11:
        print("Analista responsavel: Gilmar Batista da Silva")
        arquivo.write("Analista responsavel: Gilmar Batista da Silva\n")
    elif analista == 12:
        print("Analista responsavel: Giovanna Santos Fonseca")
        arquivo.write("Analista responsavel: Giovanna Santos Fonseca\n")
    elif analista == 13:
        print("Analista responsavel: Guilherme Alvarez Barboza")
        arquivo.write("Analista responsavel: Guilherme Alvarez Barboza\n")
    elif analista == 14:
        print("Analista responsavel: Iago Leal do Nascimento")
        arquivo.write("Analista responsavel: Iago Leal do Nascimento\n")
    elif analista == 15:
        print("Analista responsavel: Victor Mariano Rodrigues de Moura")
        arquivo.write("Analista responsavel: Victor Mariano Rodrigues de Moura\n")
    elif analista == 16:
        print("Analista responsavel: Jefferson Vieira de Melo")
        arquivo.write("Analista responsavel: Jefferson Vieira de Melo\n")
    elif analista == 17:
        print("Analista responsavel: Jefferson Vinicius Correa dos Santos")
        arquivo.write("Analista responsavel: Jefferson Vinicius Correa dos Santos\n")
    elif analista == 18:
        print("Analista responsavel:Jéssica Pellegrini Borges")
        arquivo.write("Analista responsavel: Jéssica Pellegrini Borges\n")
    elif analista == 19:
        print("Analista responsavel: Joyce de Jesus da Silva")
        arquivo.write("Analista responsavel: Joyce de Jesus da Silva\n")
    elif analista == 20:
        print("Analista responsavel: Lucas Alexandre Brito")
        arquivo.write("Analista responsavel: Lucas Alexandre Brito\n")
    elif analista == 21:
        print("Analista responsavel: Matheus Cruz Alves")
        arquivo.write("Analista responsavel: Matheus Cruz Alves\n")
    elif analista == 22:
        print("Analista responsavel: Paulo Machado")
        arquivo.write("Analista responsavel: Paulo Machado\n")
    elif analista == 23:
        print("Analista responsavel: Caique Rodrigues Terrone")
        arquivo.write("Analista responsavel: Caique Rodrigues Terrone\n")
    elif analista == 24:
        print("Analista responsavel: Rodolfo Marcel Barros e Silva")
        arquivo.write("Analista responsavel: Rodolfo Marcel Barros e Silva\n")
    elif analista == 25:
        print("Analista responsavel: Rodolfo Vilella Alves")
        arquivo.write("Analista responsavel: Rodolfo Vilella Alves\n")
    elif analista == 26:
        print("Analista responsavel: Rodrigo Oliveira Correia")
        arquivo.write("Analista responsavel: Rodrigo Oliveira Correia\n")
    elif analista == 27:
        print("Analista responsavel: Thatiane Alexandra da Silva")
        arquivo.write("Analista responsavel: Thatiane Alexandra da Silva\n")
    else:
        print("Nenhum analista encontrado :(")

    tempo = int(input("\nInforme o tempo de atendimento em minutos: "))
    arquivo.write("Tempo de atendimento: 00:{}\n".format(tempo))

    tipo = int(input('''Escolha o tipo de atendimento:
    
    [1] VPN - Não conecta.
    [2] VPN - Instalação.
    [3] Avaya - Não conecta.
    [4] Avaya - Instalação.
    [5] RN - Instalação.
    [6] Headset - Configuração.
    [7] Proxy - Configuração.
    [8] VDI - Lentidão.
    [9] VDI - Não conecta.
    [10] Genesys - Configuração.
    [11] ITX - Instalação.
    [12] P300 - Não conecta.
    [13] USD - Configuração 
    
    Informe aqui:  '''))

    if tipo == 1:
        print("Tipo de incidente: VPN não conecta.")
        arquivo.write("Tipo de incidente: VPN não conecta.\n")
    elif tipo == 2:
        print("Tipo de incidente : VPN - Instalação.")
        arquivo.write("Tipo de incidente : VPN - Instalação.\n")
    elif tipo == 3:
        print("Tipo de incidente: Avaya - Não conecta.")
        arquivo.write("Tipo de incidente: Avaya - Não conecta.\n")
    elif tipo == 4:
        print("Tipo de incidente: Avaya - Instalação.")
        arquivo.write("Tipo de incidente: Avaya - Instalação.\n")
    elif tipo == 5:
        print("Tipo de incidente: RN - Instalação.")
        arquivo.write("Tipo de incidente: RN - Instalação.\n")
    elif tipo == 6:
        print("Tipo de incidente: Headset - Configuração.")
        arquivo.write("Tipo de incidente: Headset - Configuração.\n")
    elif tipo == 7:
        print("Tipo de incidente: Proxy - Configuração.")
        arquivo.write("Tipo de incidente: Proxy - Configuração.\n")
    elif tipo == 8:
        print("Tipo de incidente: VDI - Lentidão.")
        arquivo.write("Tipo de incidente: VDI - Lentidão.\n")
    elif tipo == 9:
        print("Tipo de incidente: VDI - Não conecta.")
        arquivo.write("Tipo de incidente: VDI - Não conecta.\n")
    elif tipo == 10:
        print("Tipo de incidente: Genesys - Configuração.")
        arquivo.write("Tipo de incidente: Genesys - Configuração.\n")
    elif tipo == 11:
        print("Tipo de incidente: ITX - Instalação.")
        arquivo.write("Tipo de incidente: ITX - Instalação.\n")
    elif tipo == 12:
        print("Tipo de incidente: P300 - Não conecta.")
        arquivo.write("Tipo de incidente: P300 - Não conecta.\n")
    elif tipo == 13:
        print("Tipo de incidente: USD - Configuração.")
        arquivo.write("Tipo de incidente: USD - Configuração.\n")
    else:
        print("Problema não encontrado :(")

    print("\nStatus: Realizando testes e procedimentos ")
    arquivo.write("Status: Realizando testes e procedimentos\n ")
    print("Processando...")
    time.sleep(3)
    print(" \n ======== Registrado :D ======== \n ")
    time.sleep(3)

    arquivo.write('-=-'*24)
    arquivo.close()
