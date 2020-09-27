import database
import archiveis
import time
import traceback

def arquivar_tweets():
    lista_ids = database.recupera_ids_sem_arquivo()
    for par in lista_ids:
        url = "https://twitter.com/" + str(par[1]) + "/status/" + str(par[0])
        try:
            url_arquivo = archiveis.capture(url)
            print(url_arquivo)
            database.adiciona_arquivo(par[0], url_arquivo)
        except Exception as E:
            traceback.print_exc()
            print("Problema no arquivador principal")
            exit()

def arquivar_tweets_election():
    lista_ids = database.recupera_ids_sem_arquivo_election()
    for par in lista_ids:
        url = "https://twitter.com/" + str(par[1]) + "/status/" + str(par[0])
        try:
            url_arquivo = archiveis.capture(url)
            print(url_arquivo)
            database.adiciona_arquivo_election(par[0], url_arquivo)
        except Exception as E:
            traceback.print_exc()
            print("Problema no arquivador principal")
            exit()