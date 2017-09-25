class Transaction(object):

    def __init__(self, sender, recipient, amount):
        self._sender = sender
        self._recipient = recipient
        self._amount = amount

    @property
    def sender(self):
        return self._sender

    @property
    def recipient(self):
        return self._recipient

    @property
    def amount(self):
        return self._amount
