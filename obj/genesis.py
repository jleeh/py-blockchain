import time

from obj.block import Block


class Genesis(object):

    def __init__(self):
        self._block = Block(0, "Genesis Previous", time.time(), "")

    def block(self):
        return self._block
