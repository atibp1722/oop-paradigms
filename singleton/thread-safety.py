import threading

class ThreadSafety:
    #variable to store instance of the class
    _instance=None
    #class level lock for thread safety
    _lock=threading.Lock()

    #_new_ method needs to be override to create an instance
    def __new__(cls):
        #ensure thread safety
        with cls._lock:
            #check if instance of class created or not
            if not cls._instance:
                #create new instance of class
                cls._instance=super().__new__(cls)
        return cls._instance
    
ts=ThreadSafety()
ts1=ThreadSafety()

print(ts is ts1)
