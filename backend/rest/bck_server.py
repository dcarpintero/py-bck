from flask import Flask, jsonify, request
from backend.core.blockchain import Blockchain

app = Flask(__name__)
app.config.update(
    JSONIFY_PRETTYPRINT_REGULAR=True
)

blk = Blockchain(difficulty=3)
blk.add_node("Nakamoto", 7)
blk.mine_genesis()


@app.route('/blocks', methods=['GET'])
def get_blocks():
    return jsonify([block.__dict__ for block in blk.blocks])


@app.route('/block/<int:height>', methods=['GET'])
def get_block(height):
    if (height >= 0 and height < blk.len):
        return blk.blocks[height].to_json()

    return "INVALID_BLOCK_HEIGHT", 400


@app.route('/mempool', methods=['GET'])
def get_mempool():
    return jsonify([tx.__dict__ for tx in blk.mempool])


@app.route('/nodes', methods=['GET'])
def get_nodes():
    return jsonify([node.__dict__ for node in blk.nodes])


@app.route('/mine', methods=['POST'])
def post_mine():
    block = blk.mine_block()
    return jsonify(block.__dict__), 201


@app.route('/node', methods=['POST'])
def post_node():
    node_json = request.get_json()
    node = blk.add_node(node_json['name'], node_json['weight'])
    return jsonify(node.__dict__), 201


if __name__ == '__main__':
    app.run()
