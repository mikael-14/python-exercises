import sqlite3
import os 
import contacto as Contacto
import liga_contacto as LigaContacto

class Schema: 
    
    @staticmethod
    def exec(db):
        try:
         #No caso de a base de dados nao existir, vamos criar tabelas
            if os.path.exists(db) == False:
                Schema.createDB(db)
        except Exception as e:
            print("Erro: " + str(e))


    @staticmethod
    def createDB(db):
        con = sqlite3.connect(db)
        con.execute("PRAGMA foreign_keys = ON;")        #Issues in python3
        con.commit()
        cur = con.cursor()
        
        Contacto.createTable(cur)
        LigaContacto.createTable(cur)
        
        con.commit()

        con.close()
