import random
class Vehicle(object):

    def __init__(self, price, type, seats, name, fueleff):

        self.price = price
        self.type = type
        self.seats = seats
        self.name = name
        self.fueleff = fueleff


    def setprice(self,price):
        self.price = price
    def settype(self,type):
        self.type = type
    def setseats(self, seats):
        self.seats = seats
    def setname(self,name):
        self.name = name
    def setfueleff(self,fueleff):
        self.fueleff = fueleff

#ToString method for a vehicle
def tostring(Vehicle):
    print("Here is a/an "+Vehicle.type+". \nIt is a 2019 "+Vehicle.name+", it seats "+str(Vehicle.seats)+" \nand gets "+str(Vehicle.fueleff)+
          " miles to the gallon. \nYou can walk away with this "+Vehicle.type+" for $"+str(Vehicle.price))
    if (Vehicle.fueleff < 1):

        print("This vehicle is also electric")

from random import randrange

#Method that takes random car from list. Once we have narrowed down the list, we can use this to show the user a possible car match
def getcar(list):
    index = randrange(len(list))
    tostring(list.pop(index))

vehicleList = []

#Hans Fuhrmann Cars
vehicleList.append(Vehicle(39490, "car",5,"Dodge Challenger", 19))
vehicleList.append(Vehicle(43095, "car",5,"Dodge Charger", 20))
vehicleList.append(Vehicle(41345, "suv",7,"Dodge Durango", 22))
vehicleList.append(Vehicle(57770, "truck",5,"Ram 3500", 15))
vehicleList.append(Vehicle(36140, "truck",5,"Ram 1500", 15))
vehicleList.append(Vehicle(131800, "car",5,"BMW M6 Gran Coupe", 17))
vehicleList.append(Vehicle(59765, "suv",4,"BMW i3", 89))
vehicleList.append(Vehicle(56800, "car",5,"BMW 3 series sedan", 26))
vehicleList.append(Vehicle(86000, "suv",7,"BMW X5", 22))
vehicleList.append(Vehicle(173465, "car",4,"BMW i8", 40))
vehicleList.append(Vehicle(139700, "suv",5,"Porsche Cayenne Turbo", 17))
vehicleList.append(Vehicle(63700, "car",2,"Porsche 718 Cayman", 24))
vehicleList.append(Vehicle(334000, "car",2,"Porsche 911 GT2 RS", 24))
vehicleList.append(Vehicle(116800, "car",4,"Porsche Panemera 4s", 24))
vehicleList.append(Vehicle(150300, "car",4,"Porsche Taycan", 310))
vehicleList.append(Vehicle(10095, "car",4,"Chevy Spark", 34))
vehicleList.append(Vehicle(55795, "car",4,"Chevy Camaro", 24))
vehicleList.append(Vehicle(65180, "suv",9,"Chevy Suburban", 18))
vehicleList.append(Vehicle(52690, "truck",6,"Chevy Silverado", 20))
vehicleList.append(Vehicle(40685, "truck",5,"Chevy Colorado", 23))



#Jae Ung Kim(Volvo, Buick, Subaru, Honda)
vehicleList.append(Vehicle(59750, "suv",5,"Volvo XC90", 21))
vehicleList.append(Vehicle(46800, "suv",5,"Volvo XC60", 20))
vehicleList.append(Vehicle(40300, "suv",5,"Volvo XC40", 23))
vehicleList.append(Vehicle(59950, "car",5,"Volvo S90", 22))
vehicleList.append(Vehicle(166500, "truck",5,"Volvo VNR 640", 15))

vehicleList.append(Vehicle(50445, "car",5,"Buick Lacrosse", 25))
vehicleList.append(Vehicle(26500, "suv",5,"Buick Encore", 26))
vehicleList.append(Vehicle(38400, "suv",5,"Buick Envision", 29))
vehicleList.append(Vehicle(62200, "suv",5,"Buick Enclave", 27))
vehicleList.append(Vehicle(44145, "car",5,"Buick Regal GS", 19))

vehicleList.append(Vehicle(27995, "suv",5,"Subaru Forester", 25))
vehicleList.append(Vehicle(19995, "car",5,"Subaru Impreza", 27))
vehicleList.append(Vehicle(24995, "car",5,"Subaru Legacy", 25))
vehicleList.append(Vehicle(29295, "car",5,"Subaru Outback", 25))
vehicleList.append(Vehicle(27995, "car",4,"Subaru BRZ", 21))

vehicleList.append(Vehicle(21190, "car",5,"Honda Civic Coupe", 26))
vehicleList.append(Vehicle(33390, "car",5,"Honda Accord Hybrid", 49))
vehicleList.append(Vehicle(27990, "car",5,"Honda Insight Hybrid", 55))
vehicleList.append(Vehicle(40100, "car",6,"Honda Clarity Plugin Hybrid", 42))
vehicleList.append(Vehicle(40790, "truck",5,"Honda Ridgeline", 26))

#Pierre Frigon(Toyota, Mazda, Jeep, Tesla)
vehicleList.append(Vehicle(16595, "car", 5 , "Toyota Yaris" , 30))
vehicleList.append(Vehicle(27650, "car", 5, "Toyota Prius" , 53))
vehicleList.append(Vehicle(27990, "suv", 5, "Toyota RAV4", 25))
vehicleList.append(Vehicle(37300, "suv", 8, "Toyota Highlander", 20))
vehicleList.append(Vehicle(39625, "truck", 5, "Toyota Tundra", 14))
vehicleList.append(Vehicle(15995, "car", 5, "Mazda 3" , 29))
vehicleList.append(Vehicle(32888, "car", 5, "Mazda 6", 24))
vehicleList.append(Vehicle(38888, "suv", 5, "Mazda CX-9", 21))
vehicleList.append(Vehicle(29845, "suv", 5, "Mazda cx-5" , 24))
vehicleList.append(Vehicle(46595, "car", 2, "Mazda MX-5 RF", 26))
vehicleList.append(Vehicle(33103, "suv", 4, "Jeep Wrangler", 23))
vehicleList.append(Vehicle(31305, "suv", 5, "Jeep Cherokee" , 24))
vehicleList.append(Vehicle(27297, "suv", 5, "Jeep Compass" , 17))
vehicleList.append(Vehicle(37862, "suv", 8, "Jeep Grand Cherokee" , 21))
vehicleList.append(Vehicle(20745, "suv", 5, "Jeep Renegade", 20))
vehicleList.append(Vehicle(53400, "car", 5 , "Tesla Model 3", 999))
vehicleList.append(Vehicle(124600, "car", 7 , "Tesla Model S", 999))
vehicleList.append(Vehicle(127700, "suv", 6 , "Tesla Model X", 999))
vehicleList.append(Vehicle(257000, "car", 4 , "Tesla Roadster 2", 999))

#Kenny Cars

vehicleList.append(Vehicle(63100, "car",5,"E 300 4MATIC Sedan", 29))
vehicleList.append(Vehicle(47300, "suv",5,"GLC 300 4MATIC SUV", 27))
vehicleList.append(Vehicle(47400, "suv",5,"C 300 4MATIC Wagon", 27))
vehicleList.append(Vehicle(60200, "suv",5,"GLC 350e 4MATIC", 74))
vehicleList.append(Vehicle(60500, "car",2,"SLC 300 Roadster", 27))

vehicleList.append(Vehicle(102750, "car",4,"LC 500", 16))
vehicleList.append(Vehicle(55350, "suv",5,"RX 350", 19))
vehicleList.append(Vehicle(64500, "suv",5,"RX 450H", 31))
vehicleList.append(Vehicle(66250, "suv",7,"RX 350L", 25))
vehicleList.append(Vehicle(134200, "car",5,"LS 500H", 31))

vehicleList.append(Vehicle(72649, "truck",5,"F-150 Raptor", 18))
vehicleList.append(Vehicle(44099, "truck",6,"Super Duty F-250 XLT", 15))
vehicleList.append(Vehicle(394330, "car",5,"Ford Taurus SEL", 26))
vehicleList.append(Vehicle(17168, "car",5,"Ford SE HATCH", 39))
vehicleList.append(Vehicle(76049, "car",8,"Ford Expedition Limited MAX", 21))

vehicleList.append(Vehicle(36900, "suv",5,"Audi Q2", 37))
vehicleList.append(Vehicle(44536, "car",5,"Audi A3", 33))
vehicleList.append(Vehicle(93206, "car",5,"Audi RS 5 Coupé", 27))
vehicleList.append(Vehicle(48003, "car",5,"Audi A4 Avant", 27))
vehicleList.append(Vehicle(68537, "car",5,"Audi S4 Avant", 30))

#Tayler Verhaegen(Nissan, KIA, Volkswagen, Cadillac)
vehicleList.append(Vehicle(36498, "truck",3,"Nissan Titan", 15))
vehicleList.append(Vehicle(33198, "suv",7,"Nissan Pathfinder", 20))
vehicleList.append(Vehicle(27998, "car",5,"Nissan Altima", 27))
vehicleList.append(Vehicle(26798, "suv",5,"Nissan Rouge", 33))
vehicleList.append(Vehicle(24498, "Truck",4,"Nissan Frontier", 17))

vehicleList.append(Vehicle(20095, "suv",5,"KIA Soul", 26))
vehicleList.append(Vehicle(14795, "car",5,"KIA Rio", 29))
vehicleList.append(Vehicle(22495, "car",5,"KIA Forte", 31))
vehicleList.append(Vehicle(39995, "car",5,"KIA Stinger", 22))
vehicleList.append(Vehicle(28495, "suv",7,"KIA Sedona", 18))

vehicleList.append(Vehicle(24475, "car",4,"Volkswagen Bettle", 43))
vehicleList.append(Vehicle(22500, "car",5,"Volkswagen Golf", 30))
vehicleList.append(Vehicle(32995, "car",5,"Volkswagen Passat", 45))
vehicleList.append(Vehicle(29225, "suv",5,"Volkswagen Tiguan", 38))
vehicleList.append(Vehicle(47995, "car",5,"Volkswagen Arteon", 39))

vehicleList.append(Vehicle(87595, "suv",8,"Cadillac Escalade", 14))
vehicleList.append(Vehicle(44895, "suv",5,"Cadillac XT5", 19))
vehicleList.append(Vehicle(86870, "car",5,"Cadillac CT6 Plug In", 62))
vehicleList.append(Vehicle(46995, "car",5,"Cadillac CTS", 14))
vehicleList.append(Vehicle(68645, "car",5,"Cadillac ATS", 22))


print(len(vehicleList))
greetings_i = ("hello", "hi", "howdy", "what's up","hey", "sup")
greetings_r = ("My name is Autobot, what is your name?", "Welcome to Autobot, what can I call you?", "AUTOBOT INITIATED. ENTER NAME")
uservehicle = Vehicle(9999999, "", 0, "", 999)
def check_greeting(sentance):
    words = sentance.split()
    for word in words:
        if word.lower() in greetings_i:
            print (random.choice(greetings_r))
sentance = input("Hello\n")
check_greeting(sentance)
username = input("Name:")

name_r = ("Nice to meet you "+username, "Pleasure to meet you "+username, "Well "+username+", I am at your service")
def check_name():
    print(random.choice(name_r))
seats_i = ("seats", "seating", "seats,", "seating,")
seats_r = ("How many seats would you like?", "Most of our cars have anywhere from 2 to 8 seats, how many will you need?")
def check_seats(sentance):
    words = sentance.split()
    for word in words:
        if word.lower() in seats_i:
            print(random.choice(seats_r))
            seats = input("Seats:")
            uservehicle.setseats(seats)
fuel_i = ("fuel", "fuel efficiency", "fuels", "fuel,", "fuel efficiency,", "fuels,")
fuel_r = ("What is the worst fuel efficiency you would be okay with?")



def check_fuel(sentence):
   words = sentence.split()
   for word in words:
       if word.lower() in fuel_i:
           print(fuel_r)
           fuel_eff = input("Fuel efficiency level(in mpg): ")
           uservehicle.setfueleff(fuel_eff)

price_i = ("price", "cost", "amount", "price,", "cost,", "amount,")
price_r = ("What is the maximum you would like to spend?", "How much are you looking to spend?")


def check_price(sentence):
   words = sentence.split()
   for word in words:
       if word.lower() in price_i:
           print(random.choice(price_r))
           price = input("Price $:")
           uservehicle.setprice(price)


type_i = ("type", "function", "type,", "function,")
type_r = ("Are you looking for a car, truck or suv?", "Are you a car, truck, or suv kind of person?")
def check_type(sentance):
    words = sentance.split()
    for word in words:
        if word.lower() in type_i:
            print(random.choice(type_r))
            type = input("Car, truck, or SUV:")
            uservehicle.settype(type.lower())
check_name()
sentance = input("What are some important aspects you want in \nyour vehicle " +username+"(such as fuel efficiency, \nseating, price, or function of vehicle)?\n")

check_seats(sentance)
check_type(sentance)
check_fuel(sentance)
check_price(sentance)
#for vehicle in vehicleList:
 #   if(vehicle.type!=uservehicle.type):
  #      vehicleList.remove(vehicle)
#for vehicle in vehicleList:
 #   if(vehicle.price>int(uservehicle.price)):
  #      vehicleList.remove(vehicle)
#for vehicle in vehicleList:
 #   if(vehicle.fueleff<int(uservehicle.fueleff)):
  #      vehicleList.remove(vehicle)
print(len(vehicleList))
vehicleList = [vehicle for vehicle in vehicleList if vehicle.price <= int(uservehicle.price)]
vehicleList = [vehicle for vehicle in vehicleList if vehicle.type == uservehicle.type]
vehicleList = [vehicle for vehicle in vehicleList if vehicle.fueleff >= int(uservehicle.fueleff)]
vehicleList = [vehicle for vehicle in vehicleList if vehicle.seats >= int(uservehicle.seats)]


x = False
print("I have found "+str(len(vehicleList))+" vehicles that match your criteria!")
while(x==False):
    getcar(vehicleList)
    input("Are you happy with this vehicle?")

