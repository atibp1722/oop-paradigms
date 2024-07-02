#parent class from which child classes derived
class Animal:

    def __init__(self,name):
        self.name=name

    def make_sound(self):
        print(self.name,'makes a sound')

#child class is able to extend parent class
class Cat(Animal):

    #child class able to inherit the method of the parent class
    def make_sound(self):
        print(f'{self.name} says meow meow')

class Dog(Animal):

    def make_sound(self):
        print(f'{self.name} says woof woof')

cat=Cat('Jenni')
dog=Dog('Tommy')

cat.make_sound()
dog.make_sound()

print()

#necessary import to achieve abstraction
from abc import ABC, abstractmethod

#interface have no implementation, the child class must provide entire implementation details 

class InterfaceTest(ABC):

    @abstractmethod
    def abstract_method(self):
        pass

class ClassTest(InterfaceTest):

    def abstract_method(self):
        print('This is the implemenation of the method in interface')

class ClassTest1(InterfaceTest):

    def abstract_method(self):
        print('This is another implemenation of the method in interface')

class NoInterface:

    def message(self):
        print('Not implementing the interface method')

    #expect an object to be passed that implements the method of the interface
    def cls_abstract_method(object: InterfaceTest):
        object.abstract_method()
        print('Abstract method now implemented')

test=ClassTest()
test.abstract_method()

test1=ClassTest1()
test1.abstract_method()

""" object=ClassTest()
cls_abstract_method(object) """

print()

class Shape:

    def __init__(self,color):
        self.color=color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def shape_info(self):
        print(f'{self.__class__.__name__} is {self.color} in color')

class Square(Shape):

    def __init__(self,length,color):
        super().__init__(color)
        self.length=length
    
    def area(self):
        return self.length**2
    
    def perimeter(self):
        return 4*self.length

class Rectangle(Shape):

    def __init__(self,length,breadth,color):
        super().__init__(color)
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
rect=Rectangle(4,6,'red')
print('Rectangle area',rect.area())
print('Rectangle perimeter',rect.perimeter())
rect.shape_info()
print('-'*20)
sqr=Square(4,'blue')
print('Square area',sqr.area())
print('Square perimeter',sqr.perimeter())
sqr.shape_info()
