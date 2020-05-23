import json
import backend.util.bck_math as bck_math

from backend.block import Block
from jsonschema import validate


def test_block():
    block = Block(height=1,
                  data="I'm a mock block",
                  previous_hash=bck_math.compute_hash('previous block'),
                  difficulty=1,
                  nonce=bck_math.compute_nonce())
    assert isinstance(block, Block)


def test_block_to_json():
    with open('./schemas/schema_block.json', 'r') as f:
        schema_data = f.read()
        schema_block = json.loads(schema_data)

    block = Block(height=1,
                  data="I'm a mock block",
                  previous_hash=bck_math.compute_hash('previous block'),
                  difficulty=1,
                  nonce=bck_math.compute_nonce())

    block_json = json.loads(block.to_json())

    validate(instance=block_json, schema=schema_block)


def test_block_repr():
    block = Block(height=1,
                  data="I'm a mock block",
                  previous_hash=bck_math.compute_hash('previous block'),
                  difficulty=1,
                  nonce=bck_math.compute_nonce())
    assert block.to_json() == block.__repr__()
