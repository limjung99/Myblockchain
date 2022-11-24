from Fullnode import *
from User import *
from block import *
from Transaction import *
import time
import multiprocessing

class Myblockchain: #BlockChain
    def __init__(self): 
        self.difficulty = 0x100000000000000000
        self.fullnode_list = []
        self.usernode_list = []
    def node_setting(self): #set nodes and links 

        f = open("topology.dat","r")
        lines = f.readlines()

        #parsing
        fullnodes = []
        usernodes = []

        #set topology 
        for line in lines:
            tmp = line.replace(","," ")
            tmp = tmp.split()
            if tmp[0]=="node":
                for i in tmp:
                    if i!="node":
                        # is user_node? 
                        if 'F' in i: #full node
                            fullnodes.append(Fullnode)
                        else: #user node
                            usernodes.append(User)
            elif tmp[0]=="link":
                for i in tmp:
                    if i!="link":
                        if i[0]=="U":
                            index = int(i[1])
                            usernodes[index].add_link(int(i[-1]))
                        elif i[0]=="F":
                            index = int(i[1])
                            fullnodes[index].add_fullnode_index(int(i[-1]))
                            
        self.fullnode_list = fullnodes
        self.usernode_list = usernodes
    def run(self): #run the protocol
        # TX발생 및 전파 
        # Block mining 
        # 병렬 processing 

        for i in self.usernode_list:
            tx_list=i.generate_TX()
            index = i.return_f_index()
            for i in tx_list:
                self.fullnode_list[index].is_validate_TX(i) #tx이 유효한지 체크하여 유효하면 이웃에게 전파 
    def show_block_chain(self,index):
        pass
    def show_tx_pool(self,index):
        pass
    #Full 노드 Fi가 가장 최근의 블록 채굴 시 포함한 마지막 트랜잭션의 검증 결과
    def verity_last_tx(self,index):
        pass
    def trace(self,id,how): #specific idetifier's howmany transaction 
        pass
            

    

