import json

from backend.core.node import Node
from jsonschema import validate

node = Node(name='Nakamoto', weight=10)


def test_node_instance():   
    assert isinstance(node, Node)


def test_node_schema():
    with open('./schemas/schema_node.json', 'r') as f:
        schema_data = f.read()
        schema_node = json.loads(schema_data)

    node_json = json.loads(node.to_json())
    validate(instance=node_json, schema=schema_node)


def test_node_repr():
    assert node.to_json() == node.__repr__()
