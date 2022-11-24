from hashlib import sha256
import random as rd 
class Transacion:
    def __init__(self,input,output,modelno,manu,trading,others,price):
        self.input = input
        self.output = output
        self.identifier = rd.randint(1,999999999999999)
        self.modelNo = modelno
        self.manu_date = manu
        self.price = price
        self.trading_date = trading
        self.others = others
        
        self.trID = self.generate_hash()
    
    def generate_hash(self): 
        TX_contents =  str(self.input) + str(self.output) + str(self.identifier)+str(self.modelNo)
        +str(self.manu_date)+str(self.price)+str(self.trading_date)+str(self.others)
        TX_hash = sha256(TX_contents.encode())
        return TX_hash.hexdigest()

    

    
