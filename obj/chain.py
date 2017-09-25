class Chain(object):

    def __init__(self, blocks, latest_index):
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
