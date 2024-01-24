from src.ui.show import show 

class LigaContacto:
    contacto_origem :int
    contacto_destino :int

    def __init__(self,contacto_origem,contacto_destino) -> None:
        self.contacto_destino = contacto_destino
        self.contacto_origem = contacto_origem

    def __str__(self):
        return show('contacto origem:'+self.contacto_origem,'contacto destino:'+self.contacto_destino)

    def __repr__(self):
        return "\n" + str(self)
    
    @staticmethod
    def form():
        return LigaContacto(
            str(input("contacto origem: ")),
            str(input("contacto destino: "))
        )
    @staticmethod
    def createTable(cur):
        cur.execute('''
            CREATE TABLE IF NOT EXISTS LigaContacto (
            contacto_destino integer NOT NULL,
            contacto_origem integer NOT NULL,
            FOREIGN KEY (contacto_destino) REFERENCES contacto(numero),
            FOREIGN KEY (contacto_origem) REFERENCES contacto(numero),
            PRIMARY KEY (contacto_destino, contacto_origem)
        );
        ''')