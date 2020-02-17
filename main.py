"""Main file to execute"""
from modules.blockchain import Block, Blockchain

def main():
    """Simulate a blockchain"""
    blockchain = Blockchain(20)

    for n in range(10):
        blockchain.mine(Block("Block " + str(n+1)))

    while blockchain.head != None:
        print(blockchain.head)
        blockchain.head = blockchain.head.next

if __name__ == "__main__":
    main()