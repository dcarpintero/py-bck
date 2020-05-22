from backend.node import Node


def test_mine_block():
    node = Node(name='Nakamoto', weight=10)
    assert isinstance(node, Node)
