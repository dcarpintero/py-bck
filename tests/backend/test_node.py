import json

from backend.node import Node
from jsonschema import validate


def test_node():
    node = Node(name='Nakamoto', weight=10)
    assert isinstance(node, Node)


def test_node_to_json():
    with open('./schemas/schema_node.json', 'r') as f:
        schema_data = f.read()
        schema_node = json.loads(schema_data)

    node = Node(name='Nakamoto', weight=10)
    node_json = json.loads(node.to_json())

    validate(instance=node_json, schema=schema_node)


def test_node_repr():
    node = Node(name='Nakamoto', weight=10)
    assert node.to_json() == node.__repr__()
