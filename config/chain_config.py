import hashlib

import time

from config.wallet_config import WalletConfig
from dao.chain_dao import ChainDao
from obj.block import Block
from obj.chain import Chain
from obj.transaction import Transaction


class ChainConfig(object):

    initial_tokens = 30000
    mint_address = hashlib.sha256("Mint").hexdigest()

    chain = None

    @staticmethod
    def get_chain():
        ChainConfig.chain = ChainDao.open_chain()
        if ChainConfig.chain is None:
            ChainConfig.chain = ChainConfig.create_chain()
        return ChainConfig.chain

    @staticmethod
    def create_chain():
        genesis_transaction = Transaction(
            ChainConfig.mint_address,
            WalletConfig.create_default_wallet().address,
            ChainConfig.initial_tokens
        )
        genesis_block = Block(0, "Genesis Previous", time.time(), genesis_transaction)
        ChainConfig.chain = Chain([genesis_block], 0)
        ChainDao.write_chain(ChainConfig.chain)
        return ChainConfig.chain

    @staticmethod
    def add_block(block):
        ChainConfig.chain.blocks.append(block)
        ChainConfig.chain.latest_index = block.index
        ChainDao.write_chain(ChainConfig.chain)

    @staticmethod
    def sync_wallet(wallet):
        for block in ChainConfig.chain.blocks:
            transaction = block.transaction
            if transaction.recipient == wallet.address:
                wallet.token_amount += int(transaction.amount)
            elif transaction.sender == wallet.address:
                wallet.token_amount = wallet.token_amount - int(transaction.amount)
        return wallet
