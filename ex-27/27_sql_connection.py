import sqlite3
import os

def main():
    db = 'exemplo.db'

    #Apagar ficheiro de base de dados, se existir
    if os.path.exists(db):
        os.remove(db)

    #ligar base de dados
    con = sqlite3.connect(db)

    #Retirar cursor
    cur = con.cursor()

    #Criar tabela
    cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')

    cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','Hat',100,35.14)")
    cur.execute("INSERT INTO stocks VALUES ('2007-01-05','BUY','Socks',5,54)")
    cur.execute("INSERT INTO stocks VALUES ('2007-01-05','BUY','Socks',5,24)")

    con.commit()

    
    for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

    con.close()
    


if __name__ == '__main__':
    main()