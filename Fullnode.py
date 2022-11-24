from block import *
from ecdsa import SigningKey as sk
#TX pool에서 TX을 받고, nonce를 조절하면서 mining함 
class Fullnode:
    def __init__(self,number):
        self.mynumber = number
        self.blockchain = [] #node별 인정하는 block chain
        self.TXpool = [] #전송받는 transaction의 pool 
        #자신과 연결된 full node list 
        self.flink = []

    def add_fullnode_index(self,full_index):
        self.flink.append(full_index)
    
    def is_under_targetvalue(self,hash):
        if(hash[:5]=="00000"):
            return True
        else:
            return False

    def mining(self,targetnum):
        myblock = block(self.TXpool)
        while(True):
            tmphash = myblock.generate_hash()
            if(self.is_under_targetvalue(tmphash,targetnum)):
                return myblock
            else:
                myblock.add_nonce() #nonce++ 

    def is_validate_TX(self,pk,tx,sig):
        ans=pk.verify(sig,tx.endcode())
        return ans # true or flase를 return 

    

    



    