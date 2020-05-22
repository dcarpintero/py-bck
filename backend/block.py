import json
import datetime as date

import backend.util.bck_math as bck_math
import backend.util.bck_logging as bck_logging

LOGGER = bck_logging.init("dev")


class Block:
    """
    Block: A container made of a header and an aggregated list of transactions
    for inclusion in the blockchain. Each block header contains:
        - its position in the blockchain
        - a reference to the hash of the previous (parent) block in the chain
        - a cryptographic hash of the root of the Merkle-Tree of transactions
        - the approximate creation time of the block (seconds from Unix Epoch)
        - a unique answer to a difficult-to-solve mathematical puzzle
        - a cryptographic hash of the block metadata.
    """
    def __init__(self, height, data, previous_hash, difficulty, nonce):
        self.height = height
        self.hash_previous_block = previous_hash
        self.hash_merkle_root = bck_math.compute_hash_merkle(data)
        self.time = date.datetime.now()
        self.difficulty = difficulty
        self.nonce = nonce
        self.data = data
        self.hash = self.compute_hash()

    def compute_hash(self):
        return bck_math.hash(self.to_json())

    def to_json(self):
        return json.dumps(self.__dict__,
                          sort_keys=True,
                          default=bck_math.block_converter,
                          indent=2)

    def __repr__(self):
        return self.to_json()
