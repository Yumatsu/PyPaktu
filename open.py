import 

def startinstance(arq):
    if arq.endswith('.pce'): # Confere se o arquivo é da extenção PySauce
        abrir_arq = open(arq, 'r').readlines()

        for linha in abrir_arq: # Lê linha por linha fazendo os testes principais
            if linha.startswith("inpack "): # Importar pacotes do PySauce
                libnome = linha.split(" ")
                libnome[1] = libnome[1].replace("\n", "")
                

    else:
        print("Não foi possível abrir arquivo (Sulfixo não compatível)")


archive = str(input("Nome do arquivo: ")) # Inserir nome do arquivo
startinstance(archive)
