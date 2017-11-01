import hashlib


class Block(object):

    index = None
    previous_hash = None
    timestamp = None
    transaction = None
    block_hash = None

    def __init__(self, index, previous_hash, timestamp, transaction):
        Block.index = index
        Block.previous_hash = previous_hash
        Block.timestamp = timestamp
        Block.transaction = transaction
        Block.block_hash = hashlib\
            .sha256("{} {} {} {}".format(self.index, self.previous_hash, self.timestamp, self.transaction))\
            .hexdigest()

    @property
    def index(self):
        return self.index

    @property
    def previous_hash(self):
        return self.previous_hash

    @property
    def timestamp(self):
        return self.timestamp

    @property
    def transaction(self):
        return self.transaction

    @property
    def block_hash(self):
        return self.block_hash

