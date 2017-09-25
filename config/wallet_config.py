from dao.wallet_dao import WalletDao
from obj.wallet import Wallet


class WalletConfig(object):

    default_file_path = "wallet_store/default"
    default = None

    @staticmethod
    def get_default_wallet():
        default = open(WalletConfig.default_file_path, "r")
        address = default.read()
        wallet_dao = WalletDao(address)
        wallet = wallet_dao.open_wallet()
        if wallet is None:
            wallet = WalletConfig.create_default_wallet()
        WalletConfig.default = wallet
        return wallet

    @staticmethod
    def set_default_wallet(address):
        default = open(WalletConfig.default_file_path, "w")
        default.write(address)

    @staticmethod
    def create_default_wallet():
        default = open(WalletConfig.default_file_path, "w")
        wallet = Wallet.create_wallet()
        wallet_dao = WalletDao(wallet.address)
        default.write(wallet.address)
        wallet_dao.write_wallet(wallet)
        WalletConfig.default = wallet
        return wallet

