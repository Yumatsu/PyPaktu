import os

def startinstance(arq):
    if arq.endswith('.pce'): # Confere se o arquivo é da extenção PySauce
        abrir_arq = open(arq, 'r').readlines()
        packnames = open("packname.list", "r").readlines()

        for linha in abrir_arq: # Lê linha por linha fazendo os testes principais
            if linha.startswith("inpack "): # Importar pacotes do PySauce
                libnome = linha.split(" ")
                libnome[1] = libnome[1].replace("\n", "")
                libs = os.listdir("data/libstorage")
                print("Importando " + libnome[1] + "...")
                for pack in packnames:
                    pack = pack.split(",")
                    if libnome[1] == pack[0]:
                        print("Procurando lib correspondente: " + pack[0] + "...")
                        for lib in libs:
                            if lib == pack[1]:
                                print("Sucesso!")
                                startinstance("./data/libstorage/" + pack[1])

                    
    else:
        print("ERRO: Não foi possível abrir arquivo (Sulfixo não compatível)")


archive = str(input("Nome do arquivo: ")) # Inserir nome do arquivo
startinstance(archive)


