from block import *

#TX pool에서 TX을 받고, nonce를 조절하면서 mining함 
class Fullnode:
    def __init__(self,number) -> None:
        self.blockchain = []
        self.number = number #node index number
        self.TXpool = []

    



    