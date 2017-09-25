import hashlib
import random

import time


class Wallet(object):

    def __init__(self):
        """
            Leave parameters blank for a new wallet
        """
        self._address = hashlib.sha256(b'{}{}'.format(time.time(), random.randrange(0, 1000000))).hexdigest()
        self._token_amount = 0

    def __init__(self, address, token_amount):
        """
        :param address: existing wallet address
        :param token_amount: existing wallet amount
        """
        self._address = address
        self._token_amount = token_amount

    @property
    def token_amount(self):
        return self._token_amount

    @token_amount.setter
    def token_amount(self, value):
        self._token_amount = value

    @property
    def address(self):
        return self._address
