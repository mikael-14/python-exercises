from src.ui.show import show 

class Contacto:
    numero :int
    nome = "" 
    morada = ""

    def __init__(self,numero,nome,morada):
        self.numero = numero
        self.nome = nome
        self.morada = morada
     
    def __str__(self):
        return show('Numero:'+self.numero,'Nome:'+self.nome,'Morada:'+self.morada)

    def __repr__(self):
        return "\n" + str(self)
    
    @staticmethod
    def form():
        return Contacto(
            str(input("Numero: ")),
            str(input("Nome: ")),
            str(input("morada: "))
        )
    
    @staticmethod
    def createTable(cur):
        cur.execute('''
            CREATE TABLE IF NOT EXISTS contacto (
            numero integer PRIMARY KEY,
            nome text NOT NULL,
            morada text NULL
        );
        ''')
    
    @staticmethod
    def form():
        return Contacto(
            str(input("numero: ")),
            str(input("nome: ")),
            str(input("morada: ")),
        )