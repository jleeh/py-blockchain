import hashlib


class Block(object):
    def __init__(self, index, previous_hash, timestamp, transaction):
        self._index = index
        self._previous_hash = previous_hash
        self._timestamp = timestamp
        self._transaction = transaction
        self._block_hash = hashlib\
            .sha256("{} {} {} {}".format(self.index, self.previous_hash, self.timestamp, self.transaction))\
            .hexdigest()

    @property
    def index(self):
        return self._index

    @property
    def previous_hash(self):
        return self._previous_hash

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def transaction(self):
        return self._transaction

    @property
    def block_hash(self):
        return self._block_hash

