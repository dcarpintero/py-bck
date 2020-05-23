import json
import time
import backend.util.bck_math as bck_math
import backend.util.bck_logging as bck_logging

from backend.block import Block

LOGGER = bck_logging.init("dev")


class Node:
    """
    Node: A blockchain peer.
    """
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def mine_block(self, chain):
        block = Block(height=chain.len,
                      data="Hey! I'm block #" + str(chain.len),
                      previous_hash=chain.last_block.hash,
                      difficulty=chain.difficulty,
                      nonce=bck_math.compute_nonce())

        block, proof = self.proof_of_work(chain, block)
        chain.add_block(block, proof)

        return block

    def proof_of_work(self, chain, block):
        start = time.process_time()

        hashes_tried = 1
        proof = block.compute_hash()
        while int(proof, base=16) > chain.difficulty_target:
            block.nonce = bck_math.compute_nonce()
            proof = block.compute_hash()
            hashes_tried += 1

        time_taken = time.process_time() - start

        LOGGER.debug("Block:#{} - Miner:{} - Hashes Tried:{} - Mining Time:{}"
                     .format(block.height,
                             self.name,
                             hashes_tried,
                             time_taken))
        return(block, proof)

    def to_json(self):
        return json.dumps(self.__dict__, sort_keys=True, indent=2)

    def __repr__(self):
        return self.to_json()
