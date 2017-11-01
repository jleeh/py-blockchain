class Transaction(object):

    sender = None
    recipient = None
    amount = None

    def __init__(self, sender, recipient, amount):
        Transaction.sender = sender
        Transaction.recipient = recipient
        Transaction.amount = amount

    @property
    def sender(self):
        return self.sender

    @property
    def recipient(self):
        return self.recipient

    @property
    def amount(self):
        return self.amount
