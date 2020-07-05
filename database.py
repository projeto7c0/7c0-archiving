import database_auth

def recupera_ids_sem_arquivo():
    sql = "select idTweets, handle from mimic_tweets where archive_url is null order by idTweets DESC limit 1"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        value = cursor.fetchall()
    except Exception as E:
        print(E)
    db.close()
    return value

def adiciona_arquivo(id, url_arquivo):
    sql = "update mimic_tweets set archive_url =\""+url_arquivo+"\" where idTweets = \"" + str(id) + "\";"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
    except Exception as E:
        print(E)
    db.commit()
    db.close()
