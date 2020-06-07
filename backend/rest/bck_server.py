from flask import Flask
from backend.core.blockchain import Blockchain
import backend.util.bck_math as bck_math
import json

app = Flask(__name__)

blk = Blockchain(difficulty=3)

blk.add_node("Finney", 9)
blk.add_node("Szabo", 5)
blk.add_node("Back", 4)
blk.add_node("Nakamoto", 7)
blk.add_node("Wei", 8)

blk.mine_genesis()

num_blocks = 5
for _ in range(0, num_blocks):
    blk.mine_block()


@app.route('/tx', methods=['POST'])
def post_tx():
    return "Success", 201


@app.route('/node', methods=['POST'])
def post_node():
    return "Success", 201


@app.route('/blocks', methods=['GET'])
def get_blocks():
    return json.dumps([block.__dict__ for block in blk.blocks],
                      default=bck_math.block_converter,
                      indent=2)


@app.route('/mempool', methods=['GET'])
def get_mempool():
    return json.dumps([tx.__dict__ for tx in blk.mempool], indent=2)


@app.route('/nodes', methods=['GET'])
def get_nodes():
    return json.dumps([node.__dict__ for node in blk.nodes], indent=2)


if __name__ == '__main__':
    app.run(debug=True)
