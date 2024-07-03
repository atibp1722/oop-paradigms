#best implementation of singleton
#defines rules and behaviours for creating class [class of class]
#allow to customize class creation process to modify class attributes and methods before class actually created

from typing import Any

class MetaSingleton(type):
    #dictionary that stores instance for each sub-class of the meta class 
    _instances={}

    #_call_ method allow class instance to be called as if they were functions
    def __call__(cls):
        print('call running...')
        #check if instance already created
        if cls not in cls._instances:
            #create instance using the _call_ method of parent class's _call_ method
            instance=super().__call__()
            cls._instances[cls]=instance
        return cls._instances[cls]
    
    def __init__(cls,name,bases,dct):
        super().__init__(name,bases,dct)
        cls._instances[cls]=super().__call__()
    
    #return instance of the singleton
    def __call__(cls):
        return cls._instances[cls]

class Singleton(metaclass=MetaSingleton):

    def __init__(self):
        print('constructor of singleton...')
        self.attrib='This is a singleton'

sng=Singleton()
sng1=Singleton()
print(sng is sng1)

print('-'*15)

sngl=Singleton()
sngl1=Singleton()

print(sngl.attrib)
print(sngl1.attrib)

print(sngl is sngl1)
