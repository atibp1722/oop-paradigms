#factory method pattern
#creational design pattern
#mechanism to create objects w/o exposing instantiation logic to the client [hide creation logic from caller]
#objects are not created calling a constructor but a factory method
#objects are created through abstraction not concretion
#eg. if the class car is abstract, it can be made to be the parent of all cars [Cars->sports,offroad,utility]
#car instances can be made based only on those interfaces
#Car car1=CarFactory.create(Car.sports_car)
#client don't need to nkow how class in created, only how to call it and with what data to initialize it

import pygame
import random
from abc import ABC,abstractmethod

#base class
class Shapes(ABC):

    def __init__(self,x,y):
        self.x=x
        self.y=y

    @abstractmethod
    def draw_shape(self,surface):
        pass

#classes that will inherit the parent shape class
class Circle(Shapes):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius=random.randint(10,100)
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    #method from parent is overriden
    def draw_shape(self, surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y),self.radius)

class Rectangle(Shapes):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.length=random.randint(10,59)
        self.breadth=random.randint(10,30)
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    def draw_shape(self, surface):
        pygame.draw.rect(surface,self.color,(self.x,self.y,self.length,self.breadth))

#factory method to create instances
class ShapeFactory:

    @staticmethod
    def create_shape(shape_type,x,y):
        if shape_type=='circle':
            return Circle(x,y)
        elif shape_type=='rectangle':
            return Rectangle(x,y)
        else:
            raise ValueError('Invalid shape...')

#function to draw shapes using pygame
def main():

    pygame.init()
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption('Drawing shapes...')
    clock=pygame.time.Clock()

    shfc=ShapeFactory()
    #list to hold created shapes
    shapes=[]
    running=True

    while running:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                running=False
            #draw a shape
            elif i.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                shape_type=random.choice(['circle','rectangle'])
                shape=shfc.create_shape(shape_type,x,y)
                shapes.append(shape)
        
        screen.fill((255,255,255))

        #put the shapes in the screen
        for shape in shapes:
            shape.draw_shape(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__=='__main__':
    main()
