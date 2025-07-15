import psycopg2

class Database:
    def __init__(self):
        self.__dbName = "locadora"
        self.__user = "postgres"
        self.__host = "localhost"
        self.__password = 1234
        
        self.__conn = psycopg2.connect(
            dbname=self.__dbName,
            user=self.__user,
            host=self.__host,
            password= self.__password,
            port=5432
        )

    def execute_query(self, sql:str, params: tuple, fetch: bool , commit:bool):
        cur = self.__conn.cursor()
        
        if len(params) > 0:
            cur.execute(sql, params)
        else:
            cur.execute(sql)

        if fetch:
            results = cur.fetchall()
        else:
            results= []

        if commit:
            self.__conn.commit()
        
        cur.close()

        return results
        
