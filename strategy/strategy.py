from abc import ABC, abstractmethod

class PasswordStrategy(ABC):
    
    @abstractmethod
    def generate(self):
        pass
    
class NumericPasswordStrategy(PasswordStrategy):

    def generate(self):
        return '0123456789'

class AlphaPasswordStrategy(PasswordStrategy):

    def generate(self):
        return 'abcdefghijklmnopqrstuvwxyz'
    
class DefaultPassowordStrategy(PasswordStrategy):

    def generate(self):
        return '123abc'
    
class RandomPasswordGenerator:

    def generate_password(self,pwd_gen:PasswordStrategy):
        return pwd_gen.generate(self)
    
if __name__=='__main__':
    rpg=RandomPasswordGenerator()
    pwd=rpg.generate_password(DefaultPassowordStrategy)
    print('Randomly generated password:',pwd)
