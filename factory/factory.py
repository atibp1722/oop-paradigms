#factory method pattern
#creational design pattern
#mechanism to create objects w/o exposing instantiation logic to the client [hide creation logic from caller]
#objects are not created calling a constructor but a factory method
#objects are created through abstraction not concretion
#eg. if the class car is abstract, it can be made to be the parent of all cars [Cars->sports,offroad,utility]
#car instances can be made based only on those interfaces
#Car car1=CarFactory.create(Car.sports_car)
#cleint don't need to nkow how class in created, only how to call it and with what data to initialize it