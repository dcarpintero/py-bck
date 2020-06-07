import json
import time

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
        self.time = time.time_ns()
        self.difficulty = difficulty
        self.nonce = nonce
        self.data = data
        self.hash = self.compute_hash()

    def compute_hash(self):
        return bck_math.compute_double_hash(self.metadata)

    def is_valid_hash(self):
        return self.hash == self.compute_hash()

    def to_json(self):
        return json.dumps(self.__dict__, sort_keys=True, indent=2)

    def __repr__(self):
        return self.to_json()

    @ property
    def metadata(self):
        block_metadata = {
            'height': self.height,
            'hash_previous_block': self.hash_previous_block,
            'hash_merkle_root': bck_math.compute_hash_merkle(self.data),
            'time': self.time,
            'nonce': self.nonce
        }
        return json.dumps(block_metadata, sort_keys=True, indent=2)
