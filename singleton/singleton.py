#ensures that class has only one instance 
#provides easy global access to that instance
#control how it is instantitated
#critical regions must be entered serially (serialise the issues)

#singleton used for caching, logging, database connection, configuration access control and so on
#singleton used to control access to a shared resource
#don't allow singleton be used to provide global access to all resources

#considerations
#the class instance should ony be created when it is first needed
#singleton must be always in ready mode and loaded fast
#thread safety to ensure that multi threaded access to enure access is always controlled

#generic implementation
#the most simplest version
#constructor access needs to be controlled
#instantiation through the static method

class GenericSingleton:

    #variable to hold single class instance
    _instance=None

    #override __init__ and constructor naccess needs to be controlled
    def __init__(self):
        print('init called...')
        #raise error to prevent costructor instantiaton
        raise RuntimeError('Sorry constructor cannot be called')
    
    @classmethod
    def class_instance(cls):
        print('method called...')
        if not cls._instance:
            #new instance of the class to be created
            cls._instance=cls.__new__(cls)
        return cls._instance
    
gs=GenericSingleton()