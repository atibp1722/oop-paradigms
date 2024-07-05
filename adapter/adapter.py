#structural design pattern 
#allows conversion of interface of one class to be compatible with another
#converts source data into formats that one client can undserstand eg. xml to json using adaptors
#can help objcts with different or incompatible interaces to collaborate

#steps
#1. identify the service to create adapter for
#2. declare the client interface and how client communicates with the service
#3. define adapter class by implementing the client interface
#4. add private fields to the adapter class to store the reference of the adapter
#5. implement each method of client interface in adapter class
#6. client must always use adapter via the client interface

class EuropeanSocket:

    def volt(self):
        pass

    def neutral(self):
        pass

    def live(self):
        pass

    def earth(self):
        pass

#adaptee class
class Adapter(EuropeanSocket):

    def volt(self):
        return 220
    
    def neutral(self):
        return -1
    
    def live(self):
        return 1
    
    def earth(self):
        return 0

#target interface
class AmericanSocket:

    def volt(self):
        pass

    def neutral(self):
        pass

    def live(self):
        pass

    def earth(self):
        pass

#main adapter class
