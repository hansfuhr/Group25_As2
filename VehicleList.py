class Vehicle(object):

    def __init__(self, price, type, seats, name, fueleff):
        self.name = name
        self.price = price
        self.type = type
        self.seats = seats
        self.name = name
        self.fueleff = fueleff #in mpg



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

vehicleList.append(Vehicle(72649, "truck",5,"2019 F-150 Raptor", 17.96))
vehicleList.append(Vehicle(44099, "truck",6,"2019 Super Duty F-250 XLT", 15.00))
vehicleList.append(Vehicle(394330, "car",5,"2019 Taurus SEL", 26.13))
vehicleList.append(Vehicle(17168, "car",5,"SE HATCH", 38.56))
vehicleList.append(Vehicle(76049, "car",8,"2019 Expedition Limited MAX", 21.00))

vehicleList.append(Vehicle(36900, "suv",5,"Audi Q2", 36.80))
vehicleList.append(Vehicle(44536, "car",5,"Audi A3", 33.10))
vehicleList.append(Vehicle(93206, "car",5,"Audi RS 5 Coupé", 27.00))
vehicleList.append(Vehicle(48003, "car",5,"Audi A4 Avant", 26.70))
vehicleList.append(Vehicle(68537, "car",5,"Audi S4 Avant", 29.80))



#Next Person Cars