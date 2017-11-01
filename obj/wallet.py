import hashlib
import random

import time


class Wallet(object):

    address = None
    token_amount = None

    def __init__(self, address, token_amount):
        """
        :param address: existing wallet address
        :param token_amount: existing wallet amount
        """
        Wallet.address = address
        Wallet.token_amount = token_amount

    @staticmethod
    def create_wallet():
        return Wallet(hashlib.sha256(b'{}{}'.format(time.time(), random.randrange(0, 1000000))).hexdigest(), 0)

    @property
    def token_amount(self):
        return self.token_amount

    @token_amount.setter
    def token_amount(self, value):
        self.token_amount = value

    @property
    def address(self):
        return self.address
