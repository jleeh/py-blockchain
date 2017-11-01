from bunch import bunchify
from flask import json

from obj.block import Block
from obj.chain import Chain
from obj.wallet import Wallet
from wallet import crypter


class Contents(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)


class ChainDao(object):

    chain_file_path = "chain\obj"

    @staticmethod
    def open_chain():
        try:
            chain_file = open(ChainDao.chain_file_path, 'r')
            chain = ChainDao.to_chain(ChainDao.decode(chain_file.read()))
        except IOError:
            chain = None
        return chain

    @staticmethod
    def write_chain(chain):
        chain_file = file(ChainDao.chain_file_path, 'w')
        wallet_json = ChainDao.to_json(chain)
        chain_file.write(ChainDao.encode(wallet_json))

    @staticmethod
    def to_json(chain):
        return json.dumps(chain, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def to_chain(json_chain):
        chain = Contents(json_chain)
        blocks = bunchify(chain.blocks)
        return Chain(blocks, chain.latest_index)

    @staticmethod
    def encode(clear):
        return crypter.Crypter().encrypt(clear)

    @staticmethod
    def decode(enc):
        return crypter.Crypter().decrypt(enc)
