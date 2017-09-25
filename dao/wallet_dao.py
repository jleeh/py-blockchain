from flask import json

from obj.wallet import Wallet
from wallet import crypter


class Contents(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)


class WalletDao(object):

    def __init__(self, wallet_address):
        self._file_path = "wallet_store"
        self.wallet_file_path = "{}\{}".format(self._file_path, wallet_address)
        self._wallet_address = wallet_address

    def open_wallet(self):
        address_file = open(self.wallet_file_path, 'r')
        wallet = self.decode(address_file.read())
        return self.to_wallet(wallet)

    def write_wallet(self, wallet):
        address_file = file(self.wallet_file_path, 'w')
        wallet_json = self.to_json(wallet)
        address_file.write(self.encode(wallet_json))

    @staticmethod
    def to_json(wallet):
        return json.dumps(wallet, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def to_wallet(json_wallet):
        wallet = Contents(json_wallet)
        return Wallet(wallet._address, wallet._token_amount)

    @staticmethod
    def encode(clear):
        return crypter.Crypter().encrypt(clear)

    @staticmethod
    def decode(enc):
        return crypter.Crypter().decrypt(enc)
