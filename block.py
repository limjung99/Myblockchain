from datetime import datetime
from hashlib import sha256



class block: 
    def __init__(self,num,transactions, previous_hash, nonce = 0):
        #header 
        self.blocknumber = num
        self.merkle_root = 0
        self.previous_hash = previous_hash
        self.nonce = nonce
		# etc
        self.transactions=transactions #leaf TX 리스트 
        #머클루트 해시값 생성 
        self.merkle_root = self.generate_root(self.transactions)
    def add_nonce(self):
        self.nonce+=1

    def generate_root(transactions): 
        hash_list=[]
        for i in transactions:
            result = sha256(i.encode()).hexdigest()
            hash_list.append(result)
        while(len(hash_list)!=1):
            tmp=0
            tmp_hash_list=[]
            for i in range(len(hash_list)):
                if i%2==0 and i!=0:
                    tmp = sha256(tmp.encode()).hexdigest()
                    tmp_hash_list.append(tmp)
                    tmp=0
                else:
                    tmp+=hash_list[i]
            if(tmp>0):
                tmp_hash_list.append(sha256(tmp.encode()).hexdigest())
            hash_list = tmp_hash_list
        return hash_list[0]
                    
    def generate_hash(self): #block의 hash를 return 
        # hash the blocks contents
        block_contents =  str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()

