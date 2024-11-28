class passenger:
    id=1
    def __init__(self,tickets) -> None:
        self.passengerid=passenger.id
        passenger.id+=1
        self.nooftickets=tickets
        self.amount=0
    
    def printpassenger(self):
        print(f"pasenger id :{self.passengerid} | no of tickets:{self.nooftickets} | Amount: {self.amount}")