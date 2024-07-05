#creational design pattern used to encapsulate reusable logic of objects with many distinct parts
#separate the construction of complexobject from its representation
#design in such a way that same constructor process can cree different representations
#to create object, it must be exxecuted in a series of steps
#a series of distinct steps are exceuted in order to build the large object

class Food:

    def __init__(self):
        self.name=None
        self.price=None
        self.origin=None

    def __str__(self):
        return f'Name {self.name if self.name else 'NA'} price {self.price if self.price else 'NA'} origin {self.origin if self.origin else 'NA'}'
    
#builder class
class FoodBuilder:

    #set builder object as a parameter
    def __init__(self,food=Food()):
        self.food=food

    def set_name(self,name):
        self.food.name=name
        #self to return builder object rather than the object
        return self

    def set_price(self,price):
        self.food.price=price
        return self
    
    def set_origin(self,origin):
        self.food.origin=origin
        return self
    
    def build(self):
        return self.food
    

fb=FoodBuilder()
food=fb.build()
print(food)
