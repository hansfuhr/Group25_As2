class Vehicle(object):

    def __init__(self, price, type, seats, name, fueleff):
        self.name = name
        self.price = price
        self.type = type
        self.seats = seats
        self.name = name
        self.fueleff = fueleff



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
    #Test
print (vehicleList[4].name)


#Next Person Cars