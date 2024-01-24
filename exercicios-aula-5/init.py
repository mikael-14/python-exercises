from .src.ui.menu import Menu
from .src.db.schema import *

def main():
    db = 'exemplo.db'
    Schema.exec(db)
   
    while True:
        try:
            op = input(Menu)

            if op == "1":
               Task.form().save(cur)
            
            if op == "2":
                Project.form().save(cur)

            if op == "3":
                print("Projects: ")
                print(Project.loadAll(cur))
                print("Tasks: ")
                print(Task.loadAll(cur))
                
            if op == "0":
                break

        except Exception as e:
            print("Erro: " + str(e))

if __name__ == '__main__':
    main()