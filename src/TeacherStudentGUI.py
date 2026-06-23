import math


class caluculator:
    def __init__(self,x=10,y=2):
        self.x = x
        self.y = y

    def aduna(self):
        return self.x+self.y
    def scade(self):
        return self.x-self.y

    def inmulteste(self):
        return self.x*self.y
    def imparte(self):
        return self.x/self.y
    def setX(self,x):
        self.x=x
    def setY(self,y):
        self.y=y
    def cos(self):
        return math.cos(self.imparte())

    def menu(self):
        print("Menu")
        print(f"x:${self.x}  y:${self.y}")
        print("1.aduna")
        print("2.scade")
        print("3.inmulteste")
        print("4.imparte")
        print("5.modifica X")
        print("6.modifica Y")
        print("7.Cos din x/y")
        a=input()
        match int(a):
            case 1:
                print("suma:",self.aduna())
            case 2:
                print("dif",self.scade())
            case 3:
                print("inmultire",self.inmulteste())
            case 4:
                print("impartire",self.imparte())
            case 5:
                a=input("introdu X:")
                self.setX(float(a))
            case 6:
                self.setY(float(input("introdu Y:")))
            case 7:
                print("cos cu x/y este:",self.cos())
            case _:
                self.menu()
        self.menu()


if __name__=="__main__":
    print("prima versiune de calculator")
    calu=caluculator()
    calu.menu()

