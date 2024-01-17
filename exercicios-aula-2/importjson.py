import json


def main():
    with open('../src/large-file.json', encoding = "utf8") as f: #ao sair deste scope fecha automaticamente o ficheiro

        dic = json.load(f)

        print(type(dic))
        print(len(dic))
        for x in dic:
            print(str(type(x)))
            for key,value in x.items():
                print(key)

if __name__ == "__main__":
    main()