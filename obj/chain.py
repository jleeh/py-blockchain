import hashlib

import time

from obj.block import Block
from obj.transaction import Transaction


class Chain(object):

    def __init__(self, blocks, latest_index):
        self._mint_address = hashlib.sha256("Mint").hexdigest()
        self._blocks = blocks
        self._latest_index = latest_index

    @property
    def latest_index(self):
        return self._latest_index

    @property
    def blocks(self):
        return self._blocks

    @property
    def latest_block(self):
        return self._blocks[self._latest_index]

    @property
    def size(self):
        return self._blocks.__len__()

    def mint_tokens(self, address, amount):
        transaction = Transaction(self._mint_address, address, amount)
        block = Block(0, hashlib.sha256("Genesis").hexdigest(), time.time(), transaction)
        self.add_block(block)

    def add_block(self, block):
        self._blocks.append(block)
        self._latest_index = block.index

    def sync_wallet(self, wallet):
        for block in self._blocks:
            transaction = block.transaction
            if transaction.recipient == wallet.address:
                wallet.token_amount += transaction.amount
            elif transaction.sender == wallet.address:
                wallet.token_amount -= transaction.amount
        return wallet
