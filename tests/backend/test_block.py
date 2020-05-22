from backend.block import Block
import backend.util.bck_math as bck_math


def test_block():
    block = Block(height=1,
                  data="I'm a mock block",
                  previous_hash=bck_math.hash('previous block'),
                  difficulty=1,
                  nonce=bck_math.compute_nonce())
    assert isinstance(block, Block)
