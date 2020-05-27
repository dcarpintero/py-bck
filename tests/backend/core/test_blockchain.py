from backend.core.blockchain import Blockchain


def test_blockchain_instance():
    blk = Blockchain(difficulty=2)
    assert isinstance(blk, Blockchain)
    assert blk.len == 1


def test_blockchain_genesis():
    blk = Blockchain(difficulty=2)
    assert blk.len == 1


def test_blockchain_node():
    blk = Blockchain(difficulty=2)
    blk.add_node(name='Nakamoto', weight=10)
    assert blk.last_node.name == 'Nakamoto'
    assert blk.last_node.weight == 10


def test_blockchain_mine():
    blk = Blockchain(difficulty=2)
    blk.add_node(name='Nakamoto', weight=10)
    assert blk.len == 1
    assert blk.last_block.height == 0

    block_1 = blk.mine_block()
    assert blk.len == 2
    assert blk.last_block.height == 1

    block_2 = blk.mine_block()
    assert blk.len == 3
    assert blk.last_block.height == 2
    assert blk.last_block.hash == block_2.hash
    assert blk.last_block.hash_previous_block == block_1.hash


def test_blockchain_winning_node():
    blk = Blockchain(difficulty=2)
    blk.add_node(name='Nakamoto', weight=10)
    assert blk.winning_node().name == 'Nakamoto'
