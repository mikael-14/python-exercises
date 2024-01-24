import sqlite3
import os

class Project:

    def __init__(self,id,name,bd,ed):
        self.id = id
        self.name = name
        self.bd = bd
        self.ed = ed

    def __str__(self):
        return "(" + str(self.id) + " , " + str(self.name) + " , " + str(self.bd) + " , " + str(self.ed) + ")"

    def __repr__(self):
        return "\n" + str( self)


    @staticmethod
    def form():
        return Project(
            str(input("Id: ")),
            str(input("Name: ")),
            str(input("Beg_date: ")),
            str(input("End_date: "))
            )

    @staticmethod
    def createTable(cur):
        cur.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id integer PRIMARY KEY,
                name text NOT NULL,
                begin_date text,
                end_date text
            );
        ''')

    def save(self,cur):
        query = "INSERT INTO projects VALUES("+ self.id + ",'" + self.name + "','" + self.bd + "','" + self.ed +"' ) "
        print(query)
        cur.execute(query)

    @staticmethod
    def loadAll(cur):
        ret = []
        for row in cur.execute('SELECT * FROM projects ORDER BY id'):
            ret.append(Project(row[0],row[1],row[2],row[3]))

        return ret

    

class Task:

    def __init__(self,id,name,priority,project_id,status_id,bd,ed):
        self.id = id
        self.name = name
        self.priority = priority
        self.project_id = project_id
        self.status_id = status_id
        self.bd = bd
        self.end_date = ed

    def __str__(self):
        return "(" + str(self.id) + " , " + str(self.name) + " , " + str(self.priority) + " , " + str(self.project_id) + " , " + str(self.status_id) + " , " + str(self.bd) + " , " + str(self.end_date) + ")"

    def __repr__(self):
        return "\n" + str(self)


    @staticmethod
    def form():
        return Task(
            str(input("Id: ")),
            str(input("Name: ")),
            str(input("Priority: ")),
            str(input("Project Id: ")),
            str(input("Status Id: ")),
            str(input("Begin Date: ")),
            str(input("End Date: "))
            
        )


    @staticmethod
    def createTable(cur):
        cur.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
            id integer PRIMARY KEY,
            name text NOT NULL,
            priority integer,
            project_id integer NOT NULL,
            status_id integer NOT NULL,
            begin_date text NOT NULL,
            end_date text NOT NULL,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        );
        ''')
        
    
    def save(self, cur):
        query = "INSERT INTO tasks VALUES (" + self.id + ",'" + self.name +  "'," + self.priority + "," + self.project_id +"," + self.status_id + ",'" + self.bd + "','" + self.end_date + "' ) "
        print(query)
        cur.execute(query)

    @staticmethod
    def loadAll(cur):
        ret = []
        for row in cur.execute('SELECT * FROM tasks ORDER BY id'):
            ret.append(Task(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

        return ret

def criar_tabelas(db):
    con = sqlite3.connect(db)
    con.execute("PRAGMA foreign_keys = ON;")        #Issues in python3
    con.commit()
    cur = con.cursor()
    
    Project.createTable(cur)
    Task.createTable(cur)
    
    con.commit()

    con.close()


def main():
    db = 'exemplo.db'

    #No caso de a base de dados nao existir, vamos criar tabelas
    if os.path.exists(db) == False:
        criar_tabelas(db)
    
    #ligar base de dados
    con = sqlite3.connect(db)

    #Retirar cursor
    cur = con.cursor()

    while True:
        try:
            op = input("Menu:\n\t1. Add task\n\t2. Add project\n\t3. List\n")

            if op == "1":
               Task.form().save(cur)
            
            if op == "2":
                Project.form().save(cur)

            if op == "3":
                print("Projects: ")
                print(Project.loadAll(cur))
                print("Tasks: ")
                print(Task.loadAll(cur))

            con.commit()
        except Exception as e:
            print("Erro: " + str(e))


    con.close()
    


if __name__ == '__main__':
    main()