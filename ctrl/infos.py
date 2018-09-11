
from datetime import datetime

import MySQLdb


class Infos:

    """
        Asked when user wants to have create its app from his WS
    """
    def dbMelicoWanted(config, json_infos):

        # prepare connection...
        cnx = MySQLdb.connect(user=config.DB_USER, password=config.DB_PASS, database=config.DB_HOST)
        cursor = cnx.cursor()

        # prepare datas...
        statement = (
                "INSERT INTO " + config.DB_TABLE_REQUEST + 
                "(url, user, pass, email, date_registration) "
                "VALUES (%s, %s, %s, %s, %s)"
        )
        data = (json_infos['url'], json_infos['user'], json_infos['pass'], json_infos['email'], datetime.now())

        # send datas
        cursor.execute(statement, data)
        cnx.commit()

        # close connections
        cursor.close()
        cnx.close()