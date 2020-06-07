import json
import backend.util.bck_math as bck_math

from backend.core.block import Block
from jsonschema import validate


block = Block(height=1,
              data="I'm a mock block",
              previous_hash=bck_math.compute_hash('previous block'),
              difficulty=1,
              nonce=bck_math.compute_nonce())


def test_block_instance():
    assert isinstance(block, Block)


def test_block_schema():
    with open('./schemas/schema_block.json', 'r') as f:
        schema_data = f.read()
        schema_block = json.loads(schema_data)

    block_json = json.loads(block.to_json())
    validate(instance=block_json, schema=schema_block)


def test_block_is_valid_hash():
    assert block.is_valid_hash()


def test_block_is_not_valid_if_tampered_data():
    block.data = "I've been tampered"
    assert not block.is_valid_hash()


def test_block_is_not_valid_if_tampered_nonce():
    block.hash_previous_block = '0' * 64
    assert not block.is_valid_hash()


def test_block_is_not_valid_if_tampered_hash():
    block.hash_previous_hash = '0' * 64
    assert not block.is_valid_hash()


def test_block_repr():
    assert block.to_json() == block.__repr__()
