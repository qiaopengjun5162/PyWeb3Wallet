"""
@Project  : PyWeb3Wallet
@Author   : PaxonQiao
@Time     : 2025/1/16 16:18
@Software : PyCharm
@File     : web3_demo.py
"""

import os
from web3 import Web3
from ens import ENS
from dotenv import load_dotenv

load_dotenv()

ALCHEMY_MAINNET_URL = os.getenv("ALCHEMY_MAINNET_URL")
ALCHEMY_SEPOLIA_URL = os.getenv("ALCHEMY_SEPOLIA_URL")


def wei_to_eth(wei_value: int) -> float:
    return wei_value / 10**18


# 连接以太坊主网
provider_main = Web3.HTTPProvider(ALCHEMY_MAINNET_URL)
# 连接Sepolia测试网
provider_test = Web3.HTTPProvider(ALCHEMY_SEPOLIA_URL)
w3_main = Web3(provider_main)
w3_test = Web3(provider_test)
print(w3_main.is_connected())
print(w3_test.is_connected())

w3_main.ens = ENS.from_web3(w3_main)

ens_name = "vitalik.eth"
eth_address = w3_main.ens.address(ens_name)
if not eth_address:
    raise ValueError("Ethereum address not found")
print(f"Ethereum address: {eth_address}")

# 1. 查询vitalik在主网和Sepolia测试网的ETH余额
print("1. 查询vitalik在主网和Sepolia测试网的ETH余额")
balance_main = w3_main.eth.get_balance(eth_address)
balance_test = w3_test.eth.get_balance(eth_address)

# 将余额输出在console（主网）
print("ETH Balance of vitalik", w3_main.from_wei(balance_main, "ether"))
# 输出Sepolia测试网ETH余额
print("Sepolia ETH Balance of vitalik", w3_test.from_wei(balance_test, "ether"))

eth_amount = wei_to_eth(balance_main)
print(f"Wei: {balance_main}, ETH: {eth_amount}")

print(f"Balance: {balance_main}")
print(f"Balance: {type(balance_main)}")

block_info = w3_test.eth.get_block("latest")
print(f"Block info: {block_info}")
