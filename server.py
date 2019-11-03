from hashlib import sha256
import time
import json
class Block:
    def __init__(self,index,tranasactions,timestamp,previous_hash,nonce=0):
        self.index =index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def generate_hash(self):
        block_details=str(self.timestamp)+str(self.transactions)+str(self.previous_hash)+str(self.nonce)
        block_hash=sha256(block_details.encode())
        return block_hash.hexdigest()

    class Blockchain:
        difficulty = 2
        def  __init__(self):
              self.unconfirmed_transactions=[]
              self.chain=[]

        def createGenesis_block(self):
              genesis_block=Block(0,[],time.time(),"0")
              genesis_block.hash=genesis_block.generate_hash()
              self.chain.append(genesis_block)

        @property
        def last_block(self):
              return self.chain[-1]

        def add_block(self ,block,proof):
              previous_hash = self.last_block.hash
              if previous_hash != block.previous_hash:
                  return False
              if not Blockchain.is_valid_proof(block, proof):
                  return False
              block.hash = proof
              self.chain.append(block)
              return True
        def proof_of_work(self,block):
              block.nonce=0

              computed_hash=block.generate_hash()
              while not computed_hash.startswith('0' * Blockchain.difficulty):
                  block.nonce += 1
                  computed_hash = block.compute_hash()
              return computed_hash
        def add_trandsaction(self,transaction):
              self.unconfirmed_transactions.append(transaction)
