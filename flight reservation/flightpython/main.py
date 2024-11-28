from flight import flight
from passenger import passenger
class main:
    flightlist=[]
    def bookticket(self,currentflight,p):
        currentflight.tickets-=p.nooftickets
        priceincreased=p.nooftickets*200
        p.amount=currentflight.price*p.nooftickets
        currentflight.price+=priceincreased
        currentflight.passengerDetails.append(p)
        p.printpassenger()
        print("booked successfuly")
    
    def canclticket(self,currentflight,p):
        currentflight.tickets+=p.nooftickets
        priceincreased=p.nooftickets*200

        currentflight.price-=priceincreased
        currentflight.passengerDetails.remove(p)
        f.flightdetils()
    def printallflights(self):
        print("FlightId   Passengerid  No.of.tickets   Amount ")
        print("-----------------------------------------------")
        for flight in main.flightlist:
            1
            for pas in flight.passengerDetails:
                print(f"{flight.flightID}        {pas.passengerid}                {pas.nooftickets}              {pas.amount} ")
                
        
        
        
m=main()
flights=2
for i in range(flights):
    f=flight()
    main.flightlist.append(f)
passengerID=1
while True:
    print("1. Book 2. Cancel 3. Print")
    choice =int(input("enter the choice:"))
    match choice:
        case 1:
            flightid=int(input("enter the flight id: "))
            if flightid> len(main.flightlist):
                print("invalid flight")
                break
            currentflight=None
            for f in main.flightlist:
                if f.flightID == flightid:
                    f.flightdetils()
                    currentflight=f
                    break
            tickets=int(input("enter the number of tickets: "))
            if tickets > currentflight.tickets:
                print("No tickets")
                break
            else:
                p=passenger(tickets)
                m.bookticket(currentflight,p)
        case 2:
            flightid=int(input("enter the flught id: "))
            if flightid> len(main.flightlist):
                print("invalid flight")
                break
            currentflight=None
            for f in main.flightlist:
                if f.flightID == flightid:
                    currentflight=f
                    break
            passengerid=int(input("enter the passenger id: "))
            for p in currentflight.passengerDetails:
                if p.passengerid==passengerid:
                    m.canclticket(currentflight,p)
                    break
            else:
                print("Invalid passenger id")
                break
            
        case 3:
            m.printallflights()
        case _:
            break