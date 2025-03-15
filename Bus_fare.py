class Vehicle:
    def __init__(self, company, age , colour):
        self.company= company
        self.age = age
        self.colour=colour

    def printInfo(self):
        print("company: ",self.company)
        print("age: ",self.age)
        print("colour: ", self.colour)
    

class Bus(Vehicle):
    def __init__(self, name, Farechrage, wheels, seats,company,age,colour):
        super().__init__(company,age,colour)
        self.Farecharge= Farechrage
        self.wheels= wheels
        self.seats = seats

    def printInfoBus(self):
        self.Maintencecharge = self.Farecharge*0.1
        super().printInfo()
        print("Farecharge : " , self.seats*100)
        print("wheels: ", self.wheels)
        print("Seats: ", self.seats)
        print("Extra fees: ",self.Maintencecharge)
        print("Total fees: ", self.Maintencecharge+self.Farecharge)


sm= Bus("Stagecoach",600,10, 600000, "Mercedes", 2 ,"Black")
sm.printInfoBus()

        
