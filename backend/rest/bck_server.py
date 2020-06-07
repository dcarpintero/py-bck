from flask import Flask
from backend.core.blockchain import Blockchain
import json

app = Flask(__name__)

blk = Blockchain(difficulty=3)

blk.add_node("Finney", 9)
blk.add_node("Szabo", 5)
blk.add_node("Back", 4)
blk.add_node("Nakamoto", 7)
blk.add_node("Wei", 8)

blk.mine_genesis()


@app.route('/blocks', methods=['GET'])
def get_blocks():
    return json.dumps([block.__dict__ for block in blk.blocks], indent=2)


@app.route('/block/<height>', methods=['GET'])
def get_block(height):
    height = int(height)

    if (height >= 0 and height < blk.len):
        return blk.blocks[height].to_json()

    return "INVALID_BLOCK_HEIGHT", 400


@app.route('/mempool', methods=['GET'])
def get_mempool():
    return json.dumps([tx.__dict__ for tx in blk.mempool], indent=2)


@app.route('/nodes', methods=['GET'])
def get_nodes():
    return json.dumps([node.__dict__ for node in blk.nodes], indent=2)


@app.route('/mine', methods=['POST'])
def post_mine():
    block = blk.mine_block()
    return block.to_json(), 201


@app.route('/tx', methods=['POST'])
def post_tx():
    return "NOT_IMPLEMENTED", 501


@app.route('/node', methods=['POST'])
def post_node():
    return "NOT_IMPLEMENTED", 501


if __name__ == '__main__':
    app.run()
