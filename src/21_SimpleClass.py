

class Class1:

    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("Estou no construtor!")
    
    #decorators: https://www.programiz.com/python-programming/decorator
    @property
    def a(self):
        #print("Get a")
        return self.__a

    @a.setter
    def a(self,a):
        #print("Set a")
        self.__a = a 

    def __str__(self):
        #return self.a
        return "string da class 1 com a = " + str(self.a) + " , b= " + str(self.b)

    def __repr__(self):
        return "[" + str(self.a) + "," + str(self.b) + "]"

    @staticmethod
    def metodo_estatico(a,b):
        return a + b
    
def main():
    l = Class1(10,20)
    #l.b = 3
    print(str(l))
    print([l,l,l])
    #print(l.a)
    #l.a = 5
    #print(l)
    #print([l])

    print("Metodo estatico = " + str(Class1.metodo_estatico(2,3)))
    print(type(l))
    print(isinstance(l, str))

if __name__ == "__main__":
    main()