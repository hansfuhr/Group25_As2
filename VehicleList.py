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


#Jae Ung Kim(Volvo, Buick, Subaru, Honda)
vehicleList.append(Vehicle(59750, "suv",5,"Volvo XC90", 21.0))
vehicleList.append(Vehicle(46800, "suv",5,"Volvo XC60", 20.0))
vehicleList.append(Vehicle(40300, "suv",5,"Volvo XC40", 23.0))
vehicleList.append(Vehicle(59950, "car",5,"Volvo S90", 22.0))
vehicleList.append(Vehicle(42400, "car",5,"Volvo S60", 22.5))
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
vehicleList.append(Vehicle(28090, "car",5,"Honda Accord Sedan", 31.6))


#Pierre Frigon(Toyota, Mazda, Jeep, Tesla)
vehicleList.append(Vehicle(16595, "car", 5 , "Toyota Yaris" , 7.8))
vehicleList.append(Vehicle(27650, "car", 5, "Toyota Prius" , 4.4))
vehicleList.append(Vehicle(27990, "suv", 5, "Toyota RAV4", 9.4))
vehicleList.append(Vehicle(37300, "suv", 8, "Toyota Highlander", 11.8))
vehicleList.append(Vehicle(39625, "truck", 5, "Toyota Tundra", 16.8))
vehicleList.append(Vehicle(15995, "car", 5, "Mazda 3" , 8.0))
vehicleList.append(Vehicle(32888, "car", 5, "Mazda 6", 10.0))
vehicleList.append(Vehicle(38888, "suv", 5, "Mazda CX-9", 11.5))
vehicleList.append(Vehicle(29845, "suv", 5, "Mazda cx-5" , 9.7))
vehicleList.append(Vehicle(46595, "car", 2, "Mazda MX-5 RF", 9.1))
vehicleList.append(Vehicle(33103, "suv", 4, "Jeep Wrangler", 10.2))
vehicleList.append(Vehicle(31305, "suv", 5, "Jeep Cherokee" , 10))
vehicleList.append(Vehicle(27297, "suv", 5, "Jeep Compass" , 13.5))
vehicleList.append(Vehicle(37862, "suv", 8, "Jeep Grand Cherokee" , 11.3))
vehicleList.append(Vehicle(20745, "suv", 5, "Jeep Renegade", 11.5))
vehicleList.append(Vehicle(53400, "car", 5 , "Tesla Model 3", 0))
vehicleList.append(Vehicle(124600, "car", 7 , "Tesla Model S", 0))
vehicleList.append(Vehicle(127700, "suv", 6 , "Tesla Model X", 0))
vehicleList.append(Vehicle(257000, "car", 4 , "Tesla Roadster 2", 0))

