from blockchain import *
from block import *
import time
import multiprocessing


if __name__=="__main__":
    #myblockchain main
    blockchain = Myblockchain()
    blockchain.node_setting() #local p2p network setting 
    #blockchain.run()
    while True:
        print("service?")
        command = input()
        command = command.split(" ")
        if command[0]=="snapshot":
            if command[1]=="myBlockChain":
                #shwo all or specific full node's block chain
                blockchain.show_block_chain(command[2])
            elif command[1]=="trPool":
                blockchain.show_tx_pool(command[2])
        elif command[0]=="verifyLastTr":
            blockchain.verity_last_tx(command[1])
        elif command[0]=="trace":
            identifier = command[1]
            how = command[2]
            blockchain.trace(identifier,how)
        elif command[0]=="exit":
            break
            





  
