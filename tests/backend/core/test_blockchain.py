from backend.core.blockchain import Blockchain


def test_blockchain_instance():
    blockchain = Blockchain(difficulty=2)
    assert isinstance(blockchain, Blockchain)
    assert blockchain.len == 0


def test_blockchain_genesis():
    blockchain = Blockchain(difficulty=2)
    blockchain.add_node(name='Nakamoto', weight=10)
    blockchain.mine_block()
    assert blockchain.len == 1


def test_blockchain_node():
    blockchain = Blockchain(difficulty=2)
    blockchain.add_node(name='Nakamoto', weight=10)
    assert blockchain.last_node.name == 'Nakamoto'
    assert blockchain.last_node.weight == 10


def test_blockchain_winning_node():
    blockchain = Blockchain(difficulty=2)
    blockchain.add_node(name='Nakamoto', weight=10)
    assert blockchain.winning_node().name == 'Nakamoto'


def test_blockchain_mine():
    blockchain = Blockchain(difficulty=2)
    blockchain.add_node(name='Nakamoto', weight=10)
    assert blockchain.len == 0

    genesis = blockchain.mine_block()
    assert blockchain.len == 1
    assert blockchain.last_block.height == 0
    assert blockchain.last_block.hash_previous_block == '0' * 64

    block_1 = blockchain.mine_block()
    assert blockchain.len == 2
    assert blockchain.last_block.height == 1
    assert blockchain.last_block.hash == block_1.hash
    assert blockchain.last_block.hash_previous_block == genesis.hash

    block_2 = blockchain.mine_block()
    assert blockchain.len == 3
    assert blockchain.last_block.height == 2
    assert blockchain.last_block.hash == block_2.hash
    assert blockchain.last_block.hash_previous_block == block_1.hash
