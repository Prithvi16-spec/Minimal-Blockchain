import hashlib
import time

class Block:
    def __init__(self,index,timestamp,data,prev_hash,hash,proof_no):
        self.index = index
        self.proof_no = proof_no
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
    
    @property
    def calculate_hash(self):
        block_of_string = "{}{}{}{}{}".format(self.index, self.proof_no,
                                              self.prev_hash, self.data,
                                              self.timestamp)

        return hashlib.sha256(block_of_string.encode()).hexdigest()
    
    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof_no,
                                               self.prev_hash, self.data,
                                               self.timestamp)





        