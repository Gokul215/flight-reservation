class flight:
    id=1
    def __init__(self) -> None:
        self.tickets = 50
        self.price = 5000
        self.flightID = flight.id 
        flight.id+=1
        self.passengerDetails = []
    
    def flightdetils(self):
        print(f"flightid :{self.flightID} | Avaialable tickets: {self.tickets} |price per ticket:{self.price}")
        print("--------------------------------------------------------------------------------------------")
        
    