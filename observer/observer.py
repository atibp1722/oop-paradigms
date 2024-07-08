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
        print(f'user {self.name}, has added work by {author.name}')

class Writer:

    def __init__(self,name):
        self.name=name

    def add_title(self,title):
        pass

    def get_title(self):
        pass
    
    def subscribe(self,subscriber):
        pass

    def unsubscribe(self,subscriber):
        pass
    
    def subscribers(self):
        pass

    def notify_subscribers(self,title):
        pass