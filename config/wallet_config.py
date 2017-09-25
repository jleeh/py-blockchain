from dao.wallet_dao import WalletDao
from obj.wallet import Wallet

default_file_path = "wallet_store/default"


class WalletConfig(object):

    @staticmethod
    def get_default_wallet():
        default = open(default_file_path, "r")
        address = default.read()
        if address != "":
            wallet_dao = WalletDao(address)
            return wallet_dao.open_wallet()
        else:
            default = open(default_file_path, "w")
            wallet = Wallet()
            wallet_dao = WalletDao(wallet.address)
            default.write(wallet.address)
            wallet_dao.write_wallet(wallet)
            return wallet
