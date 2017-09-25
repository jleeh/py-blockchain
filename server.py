import time

from flask import Flask, render_template

from config.wallet_config import WalletConfig
from dao.wallet_dao import WalletDao
from obj.block import Block
from obj.wallet import Wallet
from wallet.runner import Runner

app = Flask(__name__)

wallet = None


@app.route('/', methods=["GET"])
def wallet():
    return render_template('wallet.html', address=wallet.address, tokens=wallet.token_amount)


@app.route('/send', methods=["GET"])
def send():
    return render_template('send.html', max=wallet.token_amount)


@app.route('/create-wallet', methods=["GET"])
def create_wallet():
    new_wallet = Wallet()
    wallet_dao.write_wallet(new_wallet)
    wallet = new_wallet
    return render_template(
        'wallet.html',
        address=wallet.address,
        tokens=wallet.token_amount,
        message="New wallet created!"
    )


def create_block():
    block = Block(chain.latest_index + 1, chain.latest_block.block_hash, time.time(), "")
    chain.add_block(block)
    return "First Block: {}, Second Block: {}".format(chain.blocks[0].block_hash, chain.blocks[1].block_hash)


if __name__ == '__main__':
    chain = Runner.chain(Runner())
    wallet = WalletConfig.get_default_wallet()
    wallet = chain.sync_wallet(wallet)
    wallet_dao = WalletDao(wallet.address)
    wallet_dao.write_wallet(wallet)
    app.run()
