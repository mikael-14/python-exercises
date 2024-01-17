

def main():
    while True:
        d1 = input("Digito 1:")
        d2 = input("Digito 2:")
        op = input("Escolha a operação: [+,*,/,-,^]")
        op = op.lower()
        result = False

        if op == "+" or op == "somar":
            op = "+"
            result = float(d1)+float(d2)
        elif op == "-" or op == "subtrair":
            op = "-"
            result = float(d1)-float(d2)
        elif op == "*" or op == "multiplicar":
            op = "*"
            result = float(d1)*float(d2)
        elif op == "/" or op == "dividir":
            op = "/"
            result = float(d1)/float(d2)
        elif op == "^" or op == "exponencial":
            op = "^"
            result = pow(float(d1),float(d2))
        else:
            print("Invalid operation")
        if(type(result) is not bool):
            print(f"Resultado: {d1} {op} {d2} = {result}")  # interpulação para dar replace à funcão


if __name__ == '__main__':
    main()
