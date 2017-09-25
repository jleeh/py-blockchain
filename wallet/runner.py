from obj.chain import Chain


class Runner(object):

    def __init__(self):
        self._chain = Chain([], 0)

    def chain(self):
        return self._chain
