class bike:
    def __init__(self,color,fuel,mileage,model) :
        self.color=color
        self.fuel=fuel
        self.mileage=mileage
        self.model=model
honda=bike("white","diesel",1200,12)
print(honda.mileage)