#import json
from json import dumps
import copy 

def main():
    dic = {
                "joao" : 10,
                "Emanuel" : 15,
                "Carlos" : {
                    "idade" : 20,
                    "professor": {
                            "escola" : "Lisboa",
                            "escolaridade": [8,9,[12,4,23,2]]
                    }
                },
                1000 : 100,
                "100": "a"
    }

    print(len(dic))
    print(dic.get("Carlos").get("professor"))
    print(dic.get("joao"))
    print(dic.keys())

    dic["antonio"] = 30
    dic["antonio"] = [2,3,4,2]
    print(dic)

    #del dic["Carlos"]

    print(dic)
    #exemplo deep copy
    dic_copy = copy.deepcopy(dic)
    dic_copy["joao"] = 10

    #exportar dicionario para JSON (Validar em https://jsonformatter.curiousconcept.com/#)
    print(dumps(dic,indent=4))

    for key,value in dic.items():
        print(str(key) + " --> " + str(value))


if __name__ == "__main__":
    main()