"""
@Project  : PyWeb3Wallet
@Author   : PaxonQiao
@Time     : 2025/1/16 16:18
@Software : PyCharm
@File     : web3_demo.py
"""

from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))
print(w3.is_connected())
print(w3.eth.get_balance("vitalik.eth"))
