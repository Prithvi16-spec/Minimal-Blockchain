import hashlib
import time

class Block:
    def __init__(self,index,block_data,previous_hash):
        self.index = index
        self.nonce = 0
        self.timestamp = time.time()
        self.data = block_data
        self.previous_hash = previous_hash
        self.hash = None
    
    def calculate_hash(self):
        while True:
            #Making a string for hashing
            block_hash_string = f"{self.index}{self.nonce}{self.timestamp}{self.data}{self.previous_hash}"

            #Converting the hash string into a bytes object
            encoded_block_bytes = block_hash_string.encode()

            hash_string = hashlib.sha256(encoded_block_bytes).hexdigest()

            if hash_string.startswith("0000"):
                return hash_string
            self.nonce +=1
    
    def __repr__(self):
        return f"Block(index={self.index}, timestamp={self.timestamp}, data={self.data}, previous hash={self.prev_hash}, nonce={self.nonce}"

class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.construct_genesis()

    def construct_genesis(self):
        self.add_block(previous_hash = "0000",data = self.current_data)

    def add_block(self,previous_hash,data):
        block = Block(
            index = len(self.chain),
            block_data = data,
            previous_hash=previous_hash
        )
        block.hash = block.calculate_hash()
        self.current_data=[]
        self.chain.append(block)

        return block
    
    def is_valid(self,block,previous_block):
        if block.index<=previous_block.index:
            return False
        
        if not block.hash.startswith("0000"):
            return False
        
        if block.previous_hash != previous_block.hash:
            return False
        
        if block.timestamp<= previous_block.timestamp:
            return False
        
        return True
    

        




        
    


    





   





        