import database
import archiveis
import time

lista_ids = database.recupera_100_ids()
count = 0
for par in lista_ids:
    count +=1
    url = "https://twitter.com/" + str(par[1]) + "/status/" + str(par[0])
    print(url)
    try:
        url_arquivo = archiveis.capture(url)
        print(str(count) +": " + url_arquivo)
        # database.adiciona_arquivo(par[0], url_arquivo)
    except Exception as E:
        print(E)
        print("Problema no arquivador principal")