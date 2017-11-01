class Chain(object):

    blocks = None
    latest_index = None

    def __init__(self, blocks, latest_index):
        Chain.blocks = blocks
        Chain.latest_index = latest_index

    @property
    def latest_index(self):
        return self.latest_index

    @latest_index.setter
    def latest_index(self, latest_index):
        self.latest_index = latest_index

    @property
    def blocks(self):
        return self.blocks

    @property
    def latest_block(self):
        return self.blocks[self.latest_index]

    @property
    def size(self):
        return self.blocks.__len__()
