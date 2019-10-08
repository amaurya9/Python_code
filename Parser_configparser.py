import configparser

def parserConfig(name1):
    parser=configparser.ConfigParser()
    parser.read(name1)
    print(parser.sections())
    print(parser.options("Headset"))
    print(parser.get("Headset","HFP"))

if __name__ == '__main__':
    name=input("please enter config file name")
    parserConfig(name)