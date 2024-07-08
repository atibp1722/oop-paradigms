#anstract buiness logic of a class from its implementation details so it can be plugged in
#when client has potentia conditional statements that switches between variant sof the same algorithm
#use to identify algorithm that can vary on the context
#defer decisions to the algorithm until runtime
#expose clients only to the interface of the algooeithm but never the specific implementation
#use compositions to loosely couple handler with parent class
#state- allow modification of obkect by delegetaing work to helper objects 
#where strategy makes them completely independent and completely unaware of each other
#command- allow conversion of operations into objects

#not optimal solution
class RandomPasswordGenerator:

    def generate_password(self,password_type='alpha'):
        if password_type=='alpha':
            return 'abcdefghijklmnopqrstuvwxyz'
        elif password_type=='numeric':
            return '0123456789'
        else:
            return 'abc123'

if __name__=='__main__':
    rpg=RandomPasswordGenerator()
    password=rpg.generate_password(password_type='alpha')
    print('Randomly generated password:',password)