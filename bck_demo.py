from backend.core.blockchain import Blockchain


def main():
    blk = Blockchain(difficulty=4)

    blk.add_node("Finney", 9)
    blk.add_node("Back", 5)
    blk.add_node("Nakamoto", 8)
    blk.add_node("Wei", 4)
    blk.add_node("Szabo", 7)

    num_blocks = 3
    for _ in range(0, num_blocks):
        blk.mine_block()


if __name__ == "__main__":
    main()
