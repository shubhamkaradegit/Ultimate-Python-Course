from random import randint


class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo
        
    def book(self,fro,to):
        print(f"Ticket is booked in trian no : {self.trainNo} from {fro} to {to}")
        

    def getStatus(self):
        print(f"train no: {self.trainNo} is running on time")

    def getFare(self,fro , to):
        print(f"Ticket is booked in trian no : {self.trainNo} from {fro} to {to} is {randint(222,5555)}")


t = Train(12399)
t.book("Ranpur", "Delhi")
t.getStatus()
t.getFare("Ranpur","Delhi")