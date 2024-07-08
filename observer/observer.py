#beavioral design pattern which consists of subjects and dependents
#object refered as subject which maintains a list of dependents called observers 
#and notifes them autmatically of state changes
#create notiifcation mechanism between objects 
#eg students subscribes to class events
#when event happens class notifies all students in list that event has happened
#it is utilized in model-view-controller (MVC) pattern

#observer class
class User:

    def __init__(self,name):
        self.name=name

    def update(self,title,author):
        print(f'user {self.name} has added {title} written by {author.name}')

class Writer:

    def __init__(self,name):
        self.name=name
        self.__subscribers=[]
        self.__titles=[]

    def add_title(self,title):
        self.__titles.append(title)
        self.notify_subscribers(title)

    def get_title(self):
        return self.__titles
    
    def subscribe(self,subscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self,subscriber):
        return self.__subscribers.remove(subscriber)
    
    def subscribers(self):
        return self.__subscribers

    def notify_subscribers(self,title):
        for i in self.__subscribers:
            i.update(title,self)

if __name__=='__main__':
    wrt=Writer('George Orwell')
    name1=User('admin')
    name2=User('student')
    wrt.subscribe(name1)
    wrt.subscribe(name2)
    wrt.add_title('1984')
    wrt.unsubscribe(name2)
    wrt.add_title('Animal Farm')
