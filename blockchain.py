from Fullnode import *
from User import *
from block import *
from Transaction import *
import time
import multiprocessing

class Myblockchain: #BlockChain
    def __init__(self): 
        self.fullnodes = []
        self.usernodes = []
    def node_setting(self): #set nodes and links 

        f = open("topology.dat","r")
        lines = f.readlines()
        f.close()

        #set topology 
        for line in lines:
            tmp = line.replace(","," ")
            tmp = tmp.split()
            if tmp[0]=="node":
                for i in tmp:
                    if i!="node":
                        # is user_node or full_node ? 
                        if 'F' in i: #full node
                            self.fullnodes.append(Fullnode(int(i[-1])))
                        else: #user node
                            self.usernodes.append(User(int(i[-1])))
            elif tmp[0]=="link":
                for i in tmp:
                    if i!="link":
                        if i[0]=="U":
                            index = int(i[1])
                            self.usernodes[index].add_link(int(i[-1]))
                        elif i[0]=="F":
                            index = int(i[1])
                            self.fullnodes[index].add_fullnode_index(int(i[-1]))
                            
       
    def run(self): #run the protocol-> issue, tx생성 및 node사이의 ipc 구현 
        # TX발생 및 전파 
        # Block mining 
        # 병렬 processing 
        for i in self.usernodes:
            #i번째 usernode가 생성한 k개의 tx들이 담긴 list 
            tx_list=i.generate_TX()
            #i번째 usernode와 link된 full_node의 index
            index = i.return_f_index()
            pub_key = i.return_pk()
            private_key = i.return_sk()
            for tx in tx_list:
                #tx이 유효한지 체크하여 유효하면 이웃에게 전파 pk,tx,si
                self.fullnodes[index].is_validate_TX(pub_key,tx,) 
    def show_block_chain(self,index):
        pass
    def show_tx_pool(self,index):
        pass
    #Full 노드 Fi가 가장 최근의 블록 채굴 시 포함한 마지막 트랜잭션의 검증 결과
    def verity_last_tx(self,index):
        pass
    def trace(self,id,how): #specific idetifier's howmany transaction 
        pass
            

    

