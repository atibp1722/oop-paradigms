import threading

class ThreadSingleton(type):
    #dictionary to control instantiation of the class
    _instance={}
    #class level lock for thread safety
    _lock=threading.Lock()

    #override _call_ method so that mehtod is instantiated
    def __call__(cls,*args,**kwargs):
        #ensure thread safety
        with cls._lock:
            #check if class is exist in dictionary or not
            if not cls in cls._instance:
                cls._instance[cls]=super().__call__(*args,**kwargs)
            return cls._instance[cls]

class Singleton(metaclass=ThreadSingleton):
    pass

def get_instance():
    s1=Singleton()
    print(s1)

#storing the threads
threads=[]
for i in range(10):
    t=threading.Thread(target=get_instance)
    threads.append(t)

for i in threads:
    i.start()

for t in threads:
    t.join()