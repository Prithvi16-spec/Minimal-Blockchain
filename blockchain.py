import hashlib
import time

class Block:
    def __init__(self,index,block_data,previous_hash):
        self.index = index
        self.nonce = 0
        self.timestamp = time.time()
        self.data = block_data
        self.prev_hash = previous_hash
        self.hash = None
    
    def calculate_hash(self):
        #Making a string for hashing
        block_hash_string = f"{self.index}{self.nonce}{self.timestamp}{self.data}{self.prev_hash}"

        #Converting the hash string into a bytes object
        encoded_block_bytes = block_hash_string.encode()

        hash_string = hashlib.sha256(encoded_block_bytes).hexdigest()

        while not hash_string.startswith("0000"):
            self.nonce +=1
            block_hash_string = f"{self.index}{self.nonce}{self.timestamp}{self.data}{self.prev_hash}"

            encoded_block_bytes = block_hash_string.encode()

            hash_string = hashlib.sha256(encoded_block_bytes).hexdigest()

        return hash_string
    
    def __repr__(self):
        return f"{self.index}{self.timestamp}{self.data}{self.prev_hash}{self.nonce}"

class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.construct_genesis()

    def construct_genesis(self):
        self.add_block(prev_hash = "0000",data = self.current_data)

    def add_block(self,prev_hash,data):
        block = Block(
            index = len(self.chain),
            block_data = data,
            prev_hash=prev_hash
        )
        block.hash = block.calculate_hash()
        self.current_data=[]
        self.chain.append(block)

        return block
    
    def is_valid(block,prev_block):
        if block.index<=prev_block.index:
            return False
        
        if not(block.hash.startswith("0000") and prev_block.hash.startswith("0000")):
            return False
        
        if block.prev_hash != prev_block.hash:
            return False
        
        if block.timestamp<= prev_block.timestamp:
            return False
        
        return True
    

        




        
    


    





   





        