def main():
    l = ["Joao","Joao", "Carlos", "Joaquim",44,55.4]
    print(l)
    
    for k in l:
        print(k)

    l.append("Antonio")
    print(l)
    l.insert(-2, "Joana<----") #Alterar aqui o id
    print(l)
    

    l.remove("Joao")
    
    print(l)
    print("Depois de adicionar:")
    print()
    for k in l:
        print(str(k) + " -> \t" + str(type(k)))  #Retirar conversao str para teste


    #print(l)
if __name__ == "__main__":
    main()
