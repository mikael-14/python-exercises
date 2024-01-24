from pessoa import Pessoa
from carro import Carro
from menu import Menu

def main():
    car_list = []
    person_list = []
    while True:
        i = input(Menu)
        if i == 1:
            nome = input("Nome")
            idade = input("Idade")
            person_list.append(Pessoa(nome,idade))
        elif i == "0":
            break
        else:
            print("Opção errada!")

if __name__ == '__main__':
    main()
