import database
import archiveis
import time

def arquivar_tweets():
    # print("Arquivando tweets...")
    lista_ids = database.recupera_ids_sem_arquivo()
    for par in lista_ids:
        url = "https://twitter.com/" + str(par[1]) + "/status/" + str(par[0])
        print(url)
        try:
            url_arquivo = archiveis.capture(url)
            print(url_arquivo)
            database.adiciona_arquivo(par[0], url_arquivo)
        except Exception as E:
            print(E)
            print("Problema no arquivador principal")