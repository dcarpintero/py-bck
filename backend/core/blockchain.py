import random as rand
import backend.util.bck_math as bck_math
import backend.util.bck_logging as bck_logging

from backend.core.node import Node

LOGGER = bck_logging.init("dev")


class Blockchain:
    """
    Blockchain: An ordered back-linked list of blocks
    starting with the genesis block at the root.
    """

    def __init__(self, difficulty=1):
        self.difficulty = difficulty
        self.nodes = []
        self.mempool = []
        self.blocks = []

    def add_transaction(self, transaction):
        self.mempool.append(transaction)
        LOGGER.info("Added Transaction to the Mempool: {}"
                    .format(self.last_transaction))

    def add_node(self, name, weight):
        if weight > 0:
            self.nodes.append(Node(name, weight))
            LOGGER.info("Added Node: {}".format(self.last_node))
            return self

    def add_block(self, block, proof):
        if self.is_valid_candidate_block(block, proof):
            self.blocks.append(block)
            LOGGER.info("Added Block: {}".format(block))

    def mine_genesis(self):
        if self.len == 0:
            return self.mine_block()

    def mine_block(self):
        if (len(self.nodes) > 0):
            return self.winning_node().mine_block(self)

    def winning_node(self):
        indexes = []

        for node in self.nodes:
            for _ in range(node.weight):
                indexes.append(self.nodes.index(node))

        rand.shuffle(indexes)
        winner = indexes[0]
        return self.nodes[winner]

    def is_valid(self):
        previous_block = self.blocks[0]

        for block in self.blocks:
            if not block.is_valid_hash():
                LOGGER.debug("Invalid block hash: '{}' in Block#{}".format(
                    block.hash, block.height))
                return False

            if ((block.height > 0) and
                    (block.previous_block_hash != previous_block.hash)):
                LOGGER.debug("Invalid previous hash: '{}' in Block#{}".format(
                    block.previous_block_hash, block.height))
                return False

            previous_block = block

        return True

    def is_valid_candidate_block(self, block, proof):
        if (self.len == 0):
            previous_hash = '0' * 64
        else:
            previous_hash = self.last_block.hash

        if not(proof.startswith("0" * self.difficulty)):
            LOGGER.debug("Invalid candidate: proof difficulty '{}' is < {}"
                         .format(proof, self.difficulty))
            return False

        if proof != block.compute_hash():
            LOGGER.debug("Invalid candidate: proof hash '{}' != hash '{}'"
                         .format(proof,
                                 block.compute_hash()))
            return False

        if block.height != self.len:
            LOGGER.debug("Invalid candidate: block height #{} != #{}"
                         .format(block.height,
                                 self.len))
            return False

        if block.hash_previous_block != previous_hash:
            LOGGER.debug("Invalid candidate: hash_previous_block '{}' != {}"
                         .format(block.hash_previous_block,
                                 previous_hash))
            return False

        return True

    @ property
    def difficulty_target(self):
        return bck_math.compute_difficulty_target(self.difficulty)

    @ property
    def len(self):
        return len(self.blocks)

    @ property
    def last_block(self):
        if self.blocks:
            return self.blocks[-1]

    @ property
    def last_node(self):
        if self.nodes:
            return self.nodes[-1]

    @ property
    def last_transaction(self):
        if self.mempool:
            return self.mempool[-1]
