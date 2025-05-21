from abc import*
class RBI(ABC):
    @abstractmethod
    def min_bal(self):    #abstract class since the implementation is hided
        pass
    def intrest(self):    #non abstract class since the implementation is not hided
        print("the instrest is 6.5%")
class HDFC(RBI):
    def min_bal(self):            # the values which is common to all the classes is mentioned as non abstract class 
        print ("Min bal- 0rs")    # and which changes from class to class are mentioned in abstract class.
class SBI(RBI):
    def min_bal(self):
        print ("Min bal- 1000 rs")
class kotak(RBI):
    def min_bal(self):
        print ("Min bal- 500 rs")
class karur_vaishya(RBI):
    def min_bal(self):
        print ("Min bal- 500 rs")      
h1=HDFC()
h1.min_bal()
h1.intrest()
s1=SBI()
s1.min_bal()
s1.intrest()
b1=kotak()
b1.min_bal()
b1.intrest()
b2=karur_vaishya()
b2.min_bal()
b2.intrest()
      
    