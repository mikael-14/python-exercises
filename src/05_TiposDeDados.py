def main():
    x = 5
    y = 5.0
    z = "5"
    k = 'c'
    i:int = 12                      #Declaracao explicita. Nao recomendavel   

    print("x = " + str(type(x)))
    print("y = " + str(type(y)))
    print("z = " + str(type(z)))
    print("k = " + str(type(k)))    #Atencao a este parametro

    print("i = " + str(type(i)))

    print(type(type(i)))            #Consultar documentacao python standard lib


    #print(str(x))
    #print(float(z))
    #print(float(k))                #Erro, lança uma excepção


    #convert_from_int_to_string()
if __name__ == "__main__":
    main()
