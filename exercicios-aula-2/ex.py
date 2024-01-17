def main():
    l = {}

    while True:
        i = input("Menu:\n\t1. Adicionar\n\t2. Listar\n\t3. Procurar\n\t4. Remover\n\t0. Sair\n>")

        if i == "1":
            nome = input("Nome: ")
            morada = input("Morada: ")
            telefone = input("Telefone: ")
            l[telefone] = {
                "Nome": nome,
                "Morada": morada,
                "Telefone": telefone
            }
        elif i == "2":
            for x in l:
                print("Nome: " + l[x]["Nome"] + ", Morada: " + l[x]["Morada"] + ", Telefone: " + l[x]["Telefone"])
        elif i == "3":
            nome = input("Nome: ")
            for x in l:
                if l[x]["Nome"] == nome:
                    print("Encontrei: Nome: " + l[x]["Nome"] + ", Morada: " + l[x]["Morada"] + ", Telefone: " + l[x]["Telefone"])
        elif i == "4":
            tel = input("Remover: ")
            if tel in l.keys():
                del l[tel]
                print("Apagado")
            else:
                print("Não encontrado")
        elif i == "0":
            break
        else:
            print("Opcao errada!")


if __name__ == "__main__":
    main()