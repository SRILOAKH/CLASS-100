class car:
    def __init__(self,model,color,mileage,fuel) :
        self.model=model
        self.color=color
        self.mileage=mileage
        self.fuel=fuel
benz=car(3,"white",357,"electric")
print(benz.fuel,benz.color)