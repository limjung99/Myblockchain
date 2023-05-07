import random as rd
from Transaction import Transacion
from ecdsa import SigningKey as sk
from Transaction import *

class User:
    #(k-1)차 판매의 구매자가 k차 판매의 판매자와 같다.
    def __init__(self,number):
        self.flink = 0
        self.mynumber = number
        self.product_num=3 
        #pubkey 및 sk 생성-> wallet 
        self.sk_key = sk.generate()
        self.pub_key = sk.get_verifying_key

    def add_link(self,f_index):
        self.flink=f_index
    
    def generate_TX(self): #TX list 생성 및 link full node에게 전달 
        txlist = []

        tx1 = Transacion()
        sig1 = self.sk_key.sign(tx1)
        txlist.append([tx1,self.pub_key,sig1])
    
        tx2 = Transacion()
        sig2 = self.sk_key.sign(tx2)
        txlist.append([tx2,self.pub_key,sig2])
        
        tx3 = Transacion()
        sig3 = self.sk_key.sign(tx3)
        txlist.append([tx3,self.pub_key,sig3])

        return txlist
    
    def return_f_index(self):
        return self.flink

    def return_pk(self):
        return self.pub_key

    def return_sk(self):
        return self.sk_key

        

    
    
    
    