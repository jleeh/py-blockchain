import time

import flask
from flask import Flask, render_template, redirect

from config.chain_config import ChainConfig
from config.wallet_config import WalletConfig
from obj.block import Block
from obj.transaction import Transaction
from obj.wallet import Wallet

app = Flask(__name__)


@app.route('/', methods=['GET'])
def wallet():
    Wallet.default = ChainConfig.sync_wallet(WalletConfig.get_default_wallet())
    return render_template('wallet.html', address=Wallet.default.address, tokens=Wallet.default.token_amount)


@app.route('/send', methods=['GET'])
def send():
    return render_template('send.html', max=WalletConfig.default.token_amount)


@app.route('/send', methods=['POST'])
def send_submit():
    transaction = Transaction(WalletConfig.default.address,
                              flask.request.values.get('address'),
                              flask.request.values.get('amount'))
    block = Block(
        ChainConfig.chain.latest_index + 1,
        ChainConfig.chain.blocks[ChainConfig.chain.latest_index].block_hash,
        time.time(),
        transaction
    )
    ChainConfig.add_block(block)
    return redirect("/")


@app.route('/create-wallet', methods=['GET'])
def create_wallet():
    Wallet.default = WalletConfig.create_default_wallet()
    return render_template(
        'wallet.html',
        address=Wallet.default.address,
        tokens=Wallet.default.token_amount,
        message="New wallet created!"
    )


@app.route('/load-wallet', methods=['GET'])
def load_wallet():
    return render_template('load_wallet.html')


@app.route('/load-wallet', methods=['POST'])
def load_wallet_submit():
    Wallet.default = WalletConfig.set_default_wallet(flask.request.values.get('address'))
    return redirect("/")


if __name__ == '__main__':
    ChainConfig.get_chain()
    app.run()
