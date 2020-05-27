import random as rand
import backend.util.bck_math as bck_math
import backend.util.bck_logging as bck_logging

from backend.core.block import Block
from backend.core.node import Node

LOGGER = bck_logging.init("dev")


class Blockchain:
    """
    Blockchain: An ordered back-linked list of blocks.
    """
    def __init__(self, difficulty=1):
        self.difficulty = difficulty
        self.nodes = []
        self.mempool = []
        self.blocks = [Block(height=0,
                             data="Genesis Block",
                             previous_hash=0,
                             difficulty=0,
                             nonce=0)]

    def add_transaction(self, transaction):
        self.mempool.append(transaction)
        LOGGER.info("Added Transaction to the Mempool: {}"
                    .format(self.last_transaction))

    def add_block(self, block, proof):
        if self.is_valid_block(block, proof):
            self.blocks.append(block)
            LOGGER.info("Added Block: {}".format(block))

    def add_node(self, name, weight):
        if weight > 0:
            self.nodes.append(Node(name, weight))
            LOGGER.info("Added Node: {}".format(self.last_node))
            return self

    def mine_block(self):
        return self.winning_node().mine_block(self)

    def winning_node(self):
        indexes = []

        for node in self.nodes:
            for _ in range(node.weight):
                indexes.append(self.nodes.index(node))

        rand.shuffle(indexes)
        winner = indexes[0]
        return self.nodes[winner]

    def is_valid_block(self, block, proof):
        if not(proof.startswith("0" * self.difficulty)):
            LOGGER.debug("Invalid block: proof difficulty '{}' is < {}"
                         .format(proof, self.difficulty))
            return False

        if proof != block.compute_hash():
            LOGGER.debug("Invalid block: proof hash '{}' != block hash '{}'"
                         .format(proof,
                                 block.compute_hash()))
            return False

        if block.hash_previous_block != self.last_block.hash:
            LOGGER.debug("Invalid block: hash_previous_block '{}' != {}"
                         .format(block.hash_previous_block,
                                 self.last_block.hash))
            return False

        if block.height != (self.last_block.height + 1):
            LOGGER.debug("Invalid block: block height #{} != #{}"
                         .format(block.height,
                                 self.last_block.height + 1))
            return False

        block.hash = proof
        return True

    @property
    def difficulty_target(self):
        return bck_math.compute_difficulty_target(self.difficulty)

    @property
    def len(self):
        return len(self.blocks)

    @property
    def last_block(self):
        if self.blocks:
            return self.blocks[-1]

    @property
    def last_node(self):
        if self.nodes:
            return self.nodes[-1]

    @property
    def last_transaction(self):
        if self.mempool:
            return self.mempool[-1]
