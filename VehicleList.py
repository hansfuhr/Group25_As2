class Vehicle(object):

    def __init__(self, price, type, seats, name, fueleff):
        self.name = name
        self.price = price
        self.type = type
        self.seats = seats
        self.name = name
        self.fueleff = fueleff

#ToString method for a vehicle
def tostring(Vehicle):
    print("Here is a/an "+Vehicle.type+". It is a 2019 "+Vehicle.name+", it seats "+str(Vehicle.seats)+" and gets "+str(Vehicle.fueleff)+
          " miles to the gallon. You can walk away with this "+Vehicle.type+" for $"+str(Vehicle.price))
    if (Vehicle.fueleff < 1):

        print("This vehicle is also electric")

from random import randrange

#Method that takes random car from list. Once we have narrowed down the list, we can use this to show the user a possible car match
def getcar(list):
    index = randrange(len(list))
    tostring(list.pop(index))

vehicleList = []
#Hans Fuhrmann Cars
vehicleList.append(Vehicle(39490, "car",5,"Dodge Challenger", 18.6))
vehicleList.append(Vehicle(43095, "car",5,"Dodge Charger", 20.05))
vehicleList.append(Vehicle(41345, "suv",7,"Dodge Durango", 22.15))
vehicleList.append(Vehicle(57770, "truck",5,"Ram 3500", 14.6))
vehicleList.append(Vehicle(36140, "truck",5,"Ram 1500", 15.3))
vehicleList.append(Vehicle(131800, "car",5,"BMW M6 Gran Coupe", 17.3))
vehicleList.append(Vehicle(59765, "suv",4,"BMW i3", 89))
vehicleList.append(Vehicle(56800, "car",5,"BMW 3 series sedan", 25.5))
vehicleList.append(Vehicle(86000, "suv",7,"BMW X5", 22.4))
vehicleList.append(Vehicle(173465, "car",4,"BMW i8", 40))
vehicleList.append(Vehicle(139700, "suv",5,"Porsche Cayenne Turbo", 17.15))
vehicleList.append(Vehicle(63700, "car",2,"Porsche 718 Cayman", 24.15))
vehicleList.append(Vehicle(334000, "car",2,"Porsche 911 GT2 RS", 24.05))
vehicleList.append(Vehicle(116800, "car",4,"Porsche Panemera 4s", 24.15))
vehicleList.append(Vehicle(150300, "car",4,"Porsche Taycan", 310.0))
vehicleList.append(Vehicle(10095, "car",4,"Chevy Spark", 33.8))
vehicleList.append(Vehicle(55795, "car",4,"Chevy Camaro", 23.5))
vehicleList.append(Vehicle(65180, "suv",9,"Chevy Suburban", 17.9))
vehicleList.append(Vehicle(52690, "truck",6,"Chevy Silverado", 20.0))
vehicleList.append(Vehicle(40685, "truck",5,"Chevy Colorado", 22.7))



#Jae Ung Kim(Volvo, Buick, Subaru, Honda)
vehicleList.append(Vehicle(59750, "suv",5,"Volvo XC90", 21.0))
vehicleList.append(Vehicle(46800, "suv",5,"Volvo XC60", 20.0))
vehicleList.append(Vehicle(40300, "suv",5,"Volvo XC40", 23.0))
vehicleList.append(Vehicle(59950, "car",5,"Volvo S90", 22.0))
vehicleList.append(Vehicle(166500, "truck",5,"Volvo VNR 640", 14.5))

vehicleList.append(Vehicle(50445, "car",5,"Buick Lacrosse", 25.0))
vehicleList.append(Vehicle(26500, "suv",5,"Buick Encore", 26.0))
vehicleList.append(Vehicle(38400, "suv",5,"Buick Envision", 28.5))
vehicleList.append(Vehicle(62200, "suv",5,"Buick Enclave", 27.4))
vehicleList.append(Vehicle(44145, "car",5,"Buick Regal GS", 19))

vehicleList.append(Vehicle(27995, "suv",5,"Subaru Forester", 25.3))
vehicleList.append(Vehicle(19995, "car",5,"Subaru Impreza", 27.0))
vehicleList.append(Vehicle(24995, "car",5,"Subaru Legacy", 25.0))
vehicleList.append(Vehicle(29295, "car",5,"Subaru Outback", 25.0))
vehicleList.append(Vehicle(27995, "car",4,"Subaru BRZ", 21.0))

vehicleList.append(Vehicle(21190, "car",5,"Honda Civic Coupe", 26.0))
vehicleList.append(Vehicle(33390, "car",5,"Honda Accord Hybrid", 49.0))
vehicleList.append(Vehicle(27990, "car",5,"Honda Insight Hybrid", 55.0))
vehicleList.append(Vehicle(40100, "car",6,"Honda Clarity Plugin Hybrid", 42.0))
vehicleList.append(Vehicle(40790, "truck",5,"Honda Ridgeline", 26.0))

#Pierre Frigon(Toyota, Mazda, Jeep, Tesla)
vehicleList.append(Vehicle(16595, "car", 5 , "Toyota Yaris" , 30.2))
vehicleList.append(Vehicle(27650, "car", 5, "Toyota Prius" , 53.5))
vehicleList.append(Vehicle(27990, "suv", 5, "Toyota RAV4", 25.0))
vehicleList.append(Vehicle(37300, "suv", 8, "Toyota Highlander", 19.9))
vehicleList.append(Vehicle(39625, "truck", 5, "Toyota Tundra", 14.0))
vehicleList.append(Vehicle(15995, "car", 5, "Mazda 3" , 29.4))
vehicleList.append(Vehicle(32888, "car", 5, "Mazda 6", 23.5))
vehicleList.append(Vehicle(38888, "suv", 5, "Mazda CX-9", 20.5))
vehicleList.append(Vehicle(29845, "suv", 5, "Mazda cx-5" , 24.2))
vehicleList.append(Vehicle(46595, "car", 2, "Mazda MX-5 RF", 25.8))
vehicleList.append(Vehicle(33103, "suv", 4, "Jeep Wrangler", 23.0))
vehicleList.append(Vehicle(31305, "suv", 5, "Jeep Cherokee" , 23.5))
vehicleList.append(Vehicle(27297, "suv", 5, "Jeep Compass" , 17.4))
vehicleList.append(Vehicle(37862, "suv", 8, "Jeep Grand Cherokee" , 20.8))
vehicleList.append(Vehicle(20745, "suv", 5, "Jeep Renegade", 20.4))
vehicleList.append(Vehicle(53400, "car", 5 , "Tesla Model 3", 0))
vehicleList.append(Vehicle(124600, "car", 7 , "Tesla Model S", 0))
vehicleList.append(Vehicle(127700, "suv", 6 , "Tesla Model X", 0))
vehicleList.append(Vehicle(257000, "car", 4 , "Tesla Roadster 2", 0))

#Kenny Cars

vehicleList.append(Vehicle(63100, "car",5,"E 300 4MATIC Sedan", 28.93))
vehicleList.append(Vehicle(47300, "suv",5,"GLC 300 4MATIC SUV", 27.13))
vehicleList.append(Vehicle(47400, "suv",5,"C 300 4MATIC Wagon", 27.31))
vehicleList.append(Vehicle(60200, "suv",5,"GLC 350e 4MATIC", 74.11))
vehicleList.append(Vehicle(60500, "car",2,"SLC 300 Roadster", 27.3))

vehicleList.append(Vehicle(102750, "car",4,"LC 500", 16.0))
vehicleList.append(Vehicle(55350, "suv",5,"RX 350", 19.28))
vehicleList.append(Vehicle(64500, "suv",5,"RX 450H", 31.36))
vehicleList.append(Vehicle(66250, "suv",7,"RX 350L", 25))
vehicleList.append(Vehicle(134200, "car",5,"LS 500H", 30.95))

vehicleList.append(Vehicle(72649, "truck",5,"F-150 Raptor", 17.96))
vehicleList.append(Vehicle(44099, "truck",6,"Super Duty F-250 XLT", 15.00))
vehicleList.append(Vehicle(394330, "car",5,"Ford Taurus SEL", 26.13))
vehicleList.append(Vehicle(17168, "car",5,"Ford SE HATCH", 38.56))
vehicleList.append(Vehicle(76049, "car",8,"Ford Expedition Limited MAX", 21.00))

vehicleList.append(Vehicle(36900, "suv",5,"Audi Q2", 36.80))
vehicleList.append(Vehicle(44536, "car",5,"Audi A3", 33.10))
vehicleList.append(Vehicle(93206, "car",5,"Audi RS 5 Coupé", 27.00))
vehicleList.append(Vehicle(48003, "car",5,"Audi A4 Avant", 26.70))
vehicleList.append(Vehicle(68537, "car",5,"Audi S4 Avant", 29.80))

#Tayler Verhaegen(Nissan, KIA, Volkswagen, Cadillac)
vehicleList.append(Vehicle(36498, "truck",3,"Nissan Titan", 15.0))
vehicleList.append(Vehicle(33198, "suv",7,"Nissan Pathfinder", 20.0))
vehicleList.append(Vehicle(27998, "car",5,"Nissan Altima", 27.0))
vehicleList.append(Vehicle(26798, "suv",5,"Nissan Rouge", 33.0))
vehicleList.append(Vehicle(24498, "Truck",4,"Nissan Frontier", 17.0))

vehicleList.append(Vehicle(20095, "suv",5,"KIA Soul", 26.0))
vehicleList.append(Vehicle(14795, "car",5,"KIA Rio", 29.0))
vehicleList.append(Vehicle(22495, "car",5,"KIA Forte", 31.0))
vehicleList.append(Vehicle(39995, "car",5,"KIA Stinger", 22.0))
vehicleList.append(Vehicle(28495, "suv",7,"KIA Sedona", 18.0))

vehicleList.append(Vehicle(24475, "car",4,"Volkswagen Bettle", 43.0))
vehicleList.append(Vehicle(22500, "car",5,"Volkswagen Golf", 30.2))
vehicleList.append(Vehicle(32995, "car",5,"Volkswagen Passat", 45.4))
vehicleList.append(Vehicle(29225, "suv",5,"Volkswagen Tiguan", 38.2))
vehicleList.append(Vehicle(47995, "car",5,"Volkswagen Arteon", 38.7))

vehicleList.append(Vehicle(87595, "suv",8,"Cadillac Escalade", 14.0))
vehicleList.append(Vehicle(44895, "suv",5,"Cadillac XT5", 19.0))
vehicleList.append(Vehicle(86870, "car",5,"Cadillac CT6 Plug In", 62.0))
vehicleList.append(Vehicle(46995, "car",5,"Cadillac CTS", 14.0))
vehicleList.append(Vehicle(68645, "car",5,"Cadillac ATS", 22.0))

getcar(vehicleList)